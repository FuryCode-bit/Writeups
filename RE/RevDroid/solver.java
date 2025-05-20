import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.security.KeyFactory;
import java.security.PrivateKey;
import java.security.spec.PKCS8EncodedKeySpec;
import java.util.Base64;

public class solver {
    private static final String ENCRYPTED_AES_KEY_BASE = "uuSson66CecOX83S7td96sTmlu/A5cHpnGfh0SiBQjc2ET5szregN20iplMa0xg1tfoachxXp1itW3GN+FyYOA+RQ8ki/w6FKB7ewy0ozhxCQgxsNK6IAI/LXGnr0CIBuRcXbuxariT8BdWbsVPC/pU18+kKMkX/ZWJ/7onza9/OETSnH8+vFQlhgfF+8Yo/XReiCXSMeW7J0zYDsD/uEXNcm0RJZ/4r7lsSsu+B+G4bUZ1TEPyv/p/gqrxwQyoJ9S4arOJcvuyi6aQ743w9jdiOZ7c3fM7jFblgmb1F1xEbH1504iuN6SIQLWWi3V10HK9RYcPgWyATqDG045EMJA==";
    private static final String ENCRYPTED_FLAG = "d2YSMu1nE41FlhwP6qWz7EmsAtM3z2f0BSFLJYzjpkpADExQLT2Sl3A4W7G6C0lF";

    public static void main(String[] args) throws Exception {
        // Decrypt AES key
        String aesKey = decryptAESKey();
        System.out.println("AES Key: " + aesKey);

        // Decrypt flag using AES key
        byte[] encryptedFlagBytes = Base64.getDecoder().decode(ENCRYPTED_FLAG);
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        SecretKeySpec keySpec = new SecretKeySpec(aesKey.getBytes(StandardCharsets.UTF_8), "AES");
        cipher.init(Cipher.DECRYPT_MODE, keySpec);
        String flag = new String(cipher.doFinal(encryptedFlagBytes), StandardCharsets.UTF_8);
        System.out.println("Flag: " + flag);
    }

    private static String decryptAESKey() throws Exception {
        PrivateKey privateKey = buildPrivateKey();
        byte[] encryptedKeyBytes = Base64.getDecoder().decode(ENCRYPTED_AES_KEY_BASE);
        Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] aesKeyBytes = cipher.doFinal(encryptedKeyBytes);
        return new String(aesKeyBytes, StandardCharsets.UTF_8);
    }

    private static PrivateKey buildPrivateKey() throws Exception {
        String keyPem = (partA() + partB() + partC() + partD() + partE() + partF())
                .replace("-----BEGIN PRIVATE KEY-----", "")
                .replace("-----END PRIVATE KEY-----", "")
                .replaceAll("\\s+", "");
        byte[] privateKeyBytes = Base64.getDecoder().decode(keyPem);
        PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(privateKeyBytes);
        return KeyFactory.getInstance("RSA").generatePrivate(keySpec);
    }

    private static String partA() { return "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDDIfy87yWJvbCC\n"; }
    private static String partB() { return "eCJs8OFrd9GLRxmjLkVppAvdvlAgdbeqaxOzse1tsYVe9arGpcMuxGYDPfc+K5eU\nV0zZmqcrSpcRoEKYdDMjLBxV5lucxVAngAt9v5eAkzwlmJhXaIK+NmsNnS3g5Ws0\n"; }
    private static String partC() { return "20bl+s6Fjzx//i97A3M3q1umgZdd/hxSE8XqAJfNnkII3ICz+8pJ1D92JRKcDShA\nYoaht2u5RGzHUk/dQhyZ77sHU0EcYm7I0SpiyxawSx0rlhACZBai57SbGydd4d83\n"; }
    private static String partD() { return "cHyhQERD4wiDKFTpOjgXMzx9YjhaOHCFZLsgccL3wA1ni7oQrt6OmrC1sARrkKht\nSF3AACGjAgMBAAECggEAFsO5S4VkI2Hzh1UNQcOxrgBIJu/ViC8BaWX6UxU9HdGo\n"; }
    private static String partE() { return "lVjGmfkmUjIaoCMYQvKFscgMf/upA3dsc0w3//mbNQwPpxPDkSuaklOMFA1ldLBO\n6JIh77qmqcOuNFNNZS0hIPW89Cqjy+VCkOO1WBE0KhVgIS0ooY5Ge8vMS8GPRNII\n"; }
    private static String partF() { return "khMIcJjvjlgMwmo+NCWqHMNMG0Au/eu3lv5Xg2etBdPGJJwJd4HbmCkwRpCA8vFF\nNEfqXRB8Tax/ImowoHpw1CAwl6DbRAOm0tdsBxyO0moINmT0rSwRv4IAUL6wgHIt\nANs0qnEA8iUdM2AuEYcwnQD/B81YWVWka94+AiOqGQKBgQDnbKhawvoYBACpn0D2\nnG3+qI3b36X0oe9neEidJHQkSQLABP+ejzAAQc76Ljxo5OukZfYiER9zsdXxd4UQ\npfPy5dFEI6LsFON6QhOE2Pd/WbsfXDh5qOlAQd4d93vYttONASxs57OwiZClHijI\nAQYBUo1YALjJVLWwIbuXBl3O/QKBgQDX2rq+tHenzTNIh1+30RZ0CQZt/nDBhAgH\nHejJYzfE1n+Htsmk4C4FX9BhI7U8TgY0X/uzldjQtxyxU29IxzO0IcU9xLBUkbME\ns1lHKfT5fr9My2CoiuFcV1gjfK5FJg498R8+JoQ2Jt1F6qwxB7oGbGGWsNLXQ8oz\n/Un+MZelHwKBgAwLgLuwmDm1w58Qdd4gCC2P8ko2Wrnfz8kP3p+nLRBSaH08BV3o\nT/RDeJVW4LgI6ibVU7k0MPHhmKQHt3pFWOwUgA7O2AT3lVtgowlwDXmoXu/j6eCT\nJQi+JORkZCLEaUBWhkxoxtZyYn/lkPPP8dMRy99/sh5wdUBkkRHsN+e1AoGARfCu\nf6pT9wALNN4ASrwp7VEbTzqZaGqSe1PaoJ5QbKwfyGaWsaCd6Mnh6Ae86pxRcFkF\nYmwUQ5SBbIefUFKTUzN6CIiZpd1LxyMhs2hJ4ymJbKWdXR8a5GO8wEre4LLy/GkL\neYTbY/x1x/jA8GYThY9Kk5wZxPxHIU9Z0U5aV3sCgYA+/g2voBxRRHiJ5BMJ7tQT\nM9UyhqK3iBycG4R8DX+js/OKXchLpKeMCXhiljug3Iv/kqUgUk0Dj/Hu/t8aulF1\n9kYqdOkx52EyyDnYfw+IjEkbQdV+vF2PsJLh+pF8ff7esIYBhhmBd7dE5Q+Acvcc\nUoUSHLOj1yUrY6npc+0vcQ==\n-----END PRIVATE KEY-----\n"; }
}

