# AEP-008 Security and Privacy Guide

## Core rule

A Proof Room should expose accountability without leaking private intelligence.

## Never publish by default

- secrets
- credentials
- private prompts
- protected traces
- raw personal data
- private tool logs
- regulated records
- privileged legal analysis
- sensitive security findings
- restricted operational details

## Use instead

- public-safe summaries
- evidence references
- hashes
- claim boundaries
- redaction ledgers
- role-scoped access
- private appendix references

## Room boundaries

Every room should define:

- evidence boundary
- data boundary
- tool boundary
- role boundary
- publication boundary
- retention boundary
- jurisdiction boundary

## High-risk rooms

High-risk rooms require separation of duties, rollback readiness, independent review, and audit export.
