package com.isaackogan.tiktok.shop;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.junit.jupiter.api.Test;

/** ReadmeSnippets.java is compiled by test-compile; this keeps it identical to the README. */
class ReadmeTest {
    private static String read(String path) throws IOException {
        return new String(Files.readAllBytes(Paths.get(path)), StandardCharsets.UTF_8);
    }

    @Test
    void everyReadmeJavaLineIsInTheCompiledSnippetsFile() throws IOException {
        Set<String> compiled = new HashSet<>();
        for (String l : read("src/test/java/com/isaackogan/tiktok/shop/ReadmeSnippets.java").split("\n")) {
            compiled.add(l);
        }
        Matcher m = Pattern.compile("```java\n(.*?)```", Pattern.DOTALL).matcher(read("README.md"));
        int blocks = 0;
        while (m.find()) {
            blocks++;
            for (String line : m.group(1).split("\n")) {
                if (!line.trim().isEmpty()) {
                    assertTrue(compiled.contains(line), "README line missing from ReadmeSnippets.java: " + line);
                }
            }
        }
        assertTrue(blocks >= 4, "expected the README's java blocks");
    }

    @Test
    void packagePageRequirements() throws IOException {
        String readme = read("README.md");
        for (String must : Arrays.asList(
                "Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.",
                "com.isaackogan:tiktok-shop-api:0.1.0",
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
