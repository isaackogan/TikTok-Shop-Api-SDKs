package com.isaackogan.tiktok.shop;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.junit.jupiter.api.Test;

/** readme/SnippetN.java are compiled by test-compile; this keeps them identical to the README blocks. */
class ReadmeTest {
    private static String read(String path) throws IOException {
        return new String(Files.readAllBytes(Paths.get(path)), StandardCharsets.UTF_8);
    }

    @Test
    void eachReadmeJavaBlockIsItsOwnCompiledSnippetFile() throws IOException {
        Matcher m = Pattern.compile("```java\n(.*?)```", Pattern.DOTALL).matcher(read("README.md"));
        int n = 0;
        while (m.find()) {
            n++;
            String path = "src/test/java/com/isaackogan/tiktok/shop/readme/Snippet" + n + ".java";
            String wrapper = "package com.isaackogan.tiktok.shop.readme;\n\n";
            String file = read(path);
            assertTrue(file.startsWith(wrapper), path + " must start with the package line only");
            assertEquals(m.group(1), file.substring(wrapper.length()), "README java block " + n + " differs from " + path);
            assertTrue(m.group(1).contains("import "), "README java block " + n + " carries its own imports");
        }
        assertEquals(4, n, "expected the README's java blocks");
        assertFalse(Files.exists(Paths.get("src/test/java/com/isaackogan/tiktok/shop/readme/Snippet" + (n + 1) + ".java")), "stale snippet file");
    }

    @Test
    void packagePageRequirements() throws IOException {
        String readme = read("README.md");
        for (String must : Arrays.asList(
                "Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.",
                "com.isaackogan:tiktok-shop-api:",
                "https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml",
                "has not been verified against the live API",
                "ApiException", "withShop", "instanceof", "Java 11", "TikTok Shop API")) {
            assertTrue(readme.contains(must), "README lacks: " + must);
        }
        assertFalse(readme.toLowerCase().contains("official client"), "never claim to be official");
        assertFalse(readme.toLowerCase().replace("unofficial", "").contains("official"), "the only 'official' is inside 'Unofficial'");
        assertFalse(readme.contains("!["), "no logo or image");
        assertTrue(Files.exists(Paths.get("LICENSE")));
    }
}
