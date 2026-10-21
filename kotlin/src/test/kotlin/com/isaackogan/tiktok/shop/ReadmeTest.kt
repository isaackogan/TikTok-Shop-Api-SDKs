package com.isaackogan.tiktok.shop

import java.nio.file.Files
import java.nio.file.Paths
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFalse
import kotlin.test.assertTrue

/** readme/SnippetN.kt are compiled by compileTestKotlin; this keeps them identical to the README blocks. */
class ReadmeTest {
    private fun read(path: String) = String(Files.readAllBytes(Paths.get(path)), Charsets.UTF_8)

    @Test
    fun eachReadmeKotlinBlockIsItsOwnCompiledSnippetFile() {
        val blocks = Regex("```kotlin\n(.*?)```", RegexOption.DOT_MATCHES_ALL).findAll(read("README.md")).map { it.groupValues[1] }.toList()
        val dir = "src/test/kotlin/com/isaackogan/tiktok/shop/readme"
        val wrapper = "package com.isaackogan.tiktok.shop.readme\n\n"
        blocks.forEachIndexed { i, block ->
            val path = "$dir/Snippet${i + 1}.kt"
            val file = read(path)
            assertTrue(file.startsWith(wrapper), "$path must start with the package line only")
            assertEquals(block, file.substring(wrapper.length), "README kotlin block ${i + 1} differs from $path")
            assertTrue(block.contains("import "), "README kotlin block ${i + 1} carries its own imports")
        }
        assertEquals(4, blocks.size, "expected the README's kotlin blocks")
        assertFalse(Files.exists(Paths.get("$dir/Snippet${blocks.size + 1}.kt")), "stale snippet file")
    }

    @Test
    fun packagePageRequirements() {
        val readme = read("README.md")
        for (must in listOf(
            "Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.",
            "com.isaackogan:tiktok-shop-api-kotlin:",
            "https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml",
            "has not been verified against the live API",
            "TikTokShopException", "withShop", "WebhookEvent", "JVM 11", "TikTok Shop API", "<artifactId>tiktok-shop-api-kotlin</artifactId>",
        )) assertTrue(readme.contains(must), "README lacks: $must")
        assertFalse(readme.lowercase().contains("official client"), "never claim to be official")
        assertFalse(readme.lowercase().replace("unofficial", "").contains("official"), "the only 'official' is inside 'Unofficial'")
        // No logo: the only images allowed are img.shields.io badges.
        val images = Regex("""!\[""").findAll(readme).count()
        val badges = Regex("""!\[[^\]\n]*\]\(https://img\.shields\.io/""").findAll(readme).count()
        assertEquals(images, badges, "no logo: the only images allowed are img.shields.io badges")
        assertTrue(Files.exists(Paths.get("LICENSE")))
        assertEquals(read("../LICENSE"), read("LICENSE"), "LICENSE is the repo's")
    }

    @Test
    fun publishedMetadataNamesThePackage() {
        val gradle = read("build.gradle.kts")
        for (must in listOf("tiktok-shop-api-kotlin", "MIT", "Isaac Kogan", "isaackogan/TikTok-Shop-Api-SDKs")) assertTrue(gradle.contains(must), "build.gradle.kts lacks: $must")
        // Maven Central and mvnrepository show the POM description, not the README.
        val description = Regex("""description\.set\("([^"]*)"\)""").find(gradle)?.groupValues?.get(1)
        assertTrue(description != null && description.endsWith("Unofficial. Not affiliated with or endorsed by TikTok or ByteDance."), "POM description: $description")
    }

    @Test
    fun theGradleWrapperPinsTheDistributionChecksum() {
        val props = read("gradle/wrapper/gradle-wrapper.properties")
        assertTrue(Regex("(?m)^distributionSha256Sum=[0-9a-f]{64}$").containsMatchIn(props), props)
    }
}
