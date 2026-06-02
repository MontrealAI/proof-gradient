from proof_gradient.db import SessionLocal, reset_db
from proof_gradient.security import PermissionDenied, Principal, ensure_same_tenant, require_role, authorize_tool
from proof_gradient.services import RunFabric, create_tenant


def test_rbac_blocks_low_role():
    principal = Principal(user_id="u1", tenant_id="t1", role="viewer")
    try:
        require_role(principal, "admin")
    except PermissionDenied:
        pass
    else:
        raise AssertionError("viewer should not pass admin check")


def test_cross_tenant_access_fails():
    principal = Principal(user_id="u1", tenant_id="tenant_a", role="owner")
    try:
        ensure_same_tenant(principal, "tenant_b")
    except PermissionDenied:
        pass
    else:
        raise AssertionError("cross-tenant access should fail")


def test_tool_permissions_fail_closed():
    allowed, reason = authorize_tool("send", {"read": "allowed"})
    assert allowed is False
    assert "denied" in reason


def test_demo_blocks_external_send():
    reset_db()
    with SessionLocal() as session:
        tenant = create_tenant(session, "tool-security")
        result = RunFabric(session, tenant.id).run_customer_response_demo("refund response")
        session.commit()
    assert "external send was blocked by policy" in result["proof"]["credit_assignment"]["evidence"]
