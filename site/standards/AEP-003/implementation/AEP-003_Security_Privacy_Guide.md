# AEP-003 Security and Privacy Guide

## Rule

A public ProofPacket should prove accountability without leaking private intelligence.

## Never publish by default

- secrets
- credentials
- personal data
- regulated data
- private prompts
- full sensitive traces
- security vulnerabilities
- protected operational details
- privileged analysis
- national-security-sensitive details

## Use instead

- evidence references
- hashes
- access classes
- public-safe summaries
- claim boundaries
- redaction markers
- private appendix references

## Boundary classes

- public
- private
- protected
- restricted

## Publication rule

If `contains_sensitive_data = true`, the packet must not be public.

If `access_class = public`, the packet must not contain secrets, private data, protected traces, or privileged material.
