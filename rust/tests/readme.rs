//! The README's Rust blocks are compiled: block N is exactly `examples/readme_N.rs`, which
//! `cargo build --examples` (and CI) builds. This test fails when they drift apart, imports included.
use std::fs;

fn blocks(readme: &str) -> Vec<String> {
    let mut out = vec![];
    let mut cur: Option<String> = None;
    for line in readme.lines() {
        match (&mut cur, line) {
            (None, "```rust") => cur = Some(String::new()),
            (Some(b), "```") => {
                out.push(std::mem::take(b));
                cur = None;
            }
            (Some(b), l) => {
                b.push_str(l);
                b.push('\n');
            }
            _ => {}
        }
    }
    out
}

#[test]
fn every_readme_block_is_its_own_compiled_example() {
    let readme = fs::read_to_string(concat!(env!("CARGO_MANIFEST_DIR"), "/README.md")).unwrap();
    let blocks = blocks(&readme);
    assert!(blocks.len() >= 5, "found {} rust blocks", blocks.len());
    for (i, block) in blocks.iter().enumerate() {
        let path = format!("{}/examples/readme_{}.rs", env!("CARGO_MANIFEST_DIR"), i + 1);
        let file = fs::read_to_string(&path).unwrap_or_else(|e| panic!("{path}: {e}"));
        assert_eq!(block, &file, "README block {} differs from examples/readme_{}.rs", i + 1, i + 1);
        assert!(block.contains("use tiktok_shop_api"), "block {} has no imports of its own", i + 1);
    }
    let on_disk = fs::read_dir(concat!(env!("CARGO_MANIFEST_DIR"), "/examples"))
        .unwrap()
        .filter(|e| e.as_ref().unwrap().file_name().to_string_lossy().starts_with("readme_"))
        .count();
    assert_eq!(on_disk, blocks.len(), "an examples/readme_N.rs has no README block");
}

#[test]
fn the_readme_carries_the_required_lines() {
    let readme = fs::read_to_string(concat!(env!("CARGO_MANIFEST_DIR"), "/README.md")).unwrap();
    for needle in [
        "Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.",
        "https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml",
        "cargo add tiktok-shop-api",
        "Rust 1.88",
        "has not been verified against the live API",
    ] {
        assert!(readme.contains(needle), "README lacks {needle:?}");
    }
    assert!(!readme.to_lowercase().contains("official tiktok") && !readme.to_lowercase().contains("an official"));
}
