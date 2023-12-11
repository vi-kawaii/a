import nacl from "tweetnacl"

const verifyWithNacl = ({ appPublicKey, signature, rawBody, timestamp }) => {
  return nacl.sign.detached.verify(
    Buffer.from(timestamp + rawBody),
    Buffer.from(signature, "hex"),
    Buffer.from(appPublicKey, "hex")
  )
}

/**
 * Verify that the interaction request is from Discord and intended for our bot.
 *
 * @see https://discord.com/developers/docs/interactions/receiving-and-responding#security-and-authorization
 */
export async function verifyInteractionRequest(
  request,
  appPublicKey
) {
  const signature = request.headers.get("x-signature-ed25519")
  const timestamp = request.headers.get("x-signature-timestamp")
  if (typeof signature !== "string" || typeof timestamp !== "string") {
    return { isValid: false }
  }

  const rawBody = await request.text()
  const isValidRequest = signature && timestamp && verifyWithNacl({ appPublicKey, rawBody, signature, timestamp })
  if (!isValidRequest) {
    return { isValid: false }
  }

  return {
    interaction: JSON.parse(rawBody),
    isValid: true,
  }
}
