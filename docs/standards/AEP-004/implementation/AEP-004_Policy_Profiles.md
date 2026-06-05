# AEP-004 Gate Policy Profiles

## Low-risk workflow profile

- gate_mode: automated_bounded or manual
- required_evidence_level: level_1
- required_eval_status: passed
- risk_threshold: low
- canary_required: false or limited
- rollback_required: true

## Medium-risk organizational profile

- gate_mode: manual
- required_evidence_level: level_2
- required_eval_status: passed
- risk_threshold: medium
- canary_required: true
- rollback_required: true
- challenge_window: required

## High-risk / regulated profile

- gate_mode: manual
- required_evidence_level: level_4 or level_5
- required_eval_status: passed
- risk_threshold: protected
- canary_required: true
- rollback_required: true
- challenge_window: required
- publication_rules: public-safe summary only
