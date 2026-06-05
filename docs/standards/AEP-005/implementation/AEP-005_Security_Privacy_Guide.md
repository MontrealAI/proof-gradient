# AEP-005 Security and Privacy Guide

## Core rule

A public tool receipt should prove accountability without leaking private intelligence.

## Never publish by default

- secrets
- credentials
- private prompts
- sensitive personal data
- regulated data
- private API payloads
- privileged security notes
- protected evidence
- customer confidential information

## Use instead

- public-safe summaries
- hashes
- evidence references
- permission classes
- decision records
- receipt references
- redaction markers
- access classes

## High-risk permissions

The following require elevated controls:

- send
- delete
- deploy
- payment
- secret_access
- admin_change
- protected_operation
- break_glass

## Fail-closed principle

If the Tool Gateway cannot evaluate a request, it must deny or require approval.
