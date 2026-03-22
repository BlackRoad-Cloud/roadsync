# RoadSync — TODO

## [RC] Core Sync Engine
- [ ] [RC] Implement Automerge CRDT merge engine
- [ ] [RC] Build vector clock for causal ordering
- [ ] [RC] Implement file watcher with debounced change detection
- [ ] [RC] Build content-addressed deduplication layer
- [ ] [RC] Add zstd compression for transfer and storage

## [RC] Storage Backend
- [ ] [RC] MinIO integration for S3-compatible object storage
- [ ] [RC] Implement bucket management (docs, media, backups, configs)
- [ ] [RC] Build chunked upload for large files
- [ ] [RC] Add storage quota management and reporting
- [ ] [RC] Implement garbage collection for orphaned chunks

## [RC] Encryption
- [ ] [RC] Implement XChaCha20-Poly1305 client-side encryption
- [ ] [RC] Build Argon2id key derivation from passphrase
- [ ] [RC] Add key rotation without re-encrypting all files
- [ ] [RC] Implement secure key sharing for team sync
- [ ] [RC] Build zero-knowledge proof of storage

## [RC] Cross-Platform Clients
- [ ] [RC] Build macOS desktop client (Swift/SwiftUI)
- [ ] [RC] Build Linux CLI client (Rust)
- [ ] [RC] Build Windows desktop client
- [ ] [RC] Build iOS mobile client (Swift)
- [ ] [RC] Build Android mobile client (Kotlin)

## [RC] Transport & Networking
- [ ] [RC] WireGuard transport layer for LAN sync
- [ ] [RC] NAT traversal for remote device sync
- [ ] [RC] Implement bandwidth throttling and scheduling
- [ ] [RC] Build relay server for devices behind strict NAT
- [ ] [RC] Add selective sync (per-folder, per-device)

## [RC] Version History
- [ ] [RC] Build version log with vector clock metadata
- [ ] [RC] Implement point-in-time restore
- [ ] [RC] Add diff viewer for text file versions
- [ ] [RC] Build retention policy engine
- [ ] [RC] Implement version pruning to reclaim storage
