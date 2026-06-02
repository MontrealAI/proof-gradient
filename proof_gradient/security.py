from dataclasses import dataclass


ROLE_ORDER = {"viewer": 1, "operator": 2, "reviewer": 3, "admin": 4, "owner": 5}
TOOL_PERMISSION_CLASSES = {"read", "draft", "write", "send", "delete", "publish", "payment", "deploy", "external_contact", "secret_access", "admin_change"}


class PermissionDenied(RuntimeError):
    pass


@dataclass(frozen=True)
class Principal:
    user_id: str
    tenant_id: str
    role: str


def require_role(principal: Principal, required: str) -> None:
    if ROLE_ORDER.get(principal.role, 0) < ROLE_ORDER[required]:
        raise PermissionDenied(f"role {principal.role!r} cannot perform {required!r} action")


def ensure_same_tenant(principal: Principal, tenant_id: str) -> None:
    if principal.tenant_id != tenant_id:
        raise PermissionDenied("cross-tenant access denied")


def authorize_tool(permission_class: str, policy_permissions: dict[str, str]) -> tuple[bool, str]:
    if permission_class not in TOOL_PERMISSION_CLASSES:
        return False, "unknown permission class"
    decision = policy_permissions.get(permission_class, "denied")
    if decision == "allowed":
        return True, "allowed by policy"
    if decision == "approval_required":
        return False, "human approval required"
    return False, "denied by default"
