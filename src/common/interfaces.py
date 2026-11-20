"""Placeholder interfaces for cross-task integration."""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class JointState:
    names: tuple[str, ...]
    positions: tuple[float, ...]
    velocities: tuple[float, ...]


@dataclass(frozen=True)
class Pose:
    position: tuple[float, float, float]
    quaternion_wxyz: tuple[float, float, float, float]


@dataclass(frozen=True)
class Plan:
    mode: Literal["left", "right", "bimanual"]
    arms: tuple[str, ...]
    objects: tuple[str, ...]
    target: str


def solve_inverse_kinematics(_arm: str, _target: Pose) -> JointState:
    """Placeholder for Task 2 arm inverse kinematics."""
    raise NotImplementedError


def plan_base_motion(_start: Pose, _goal: Pose) -> tuple[Pose, ...]:
    """Placeholder for Task 1 base motion planning."""
    raise NotImplementedError


def grasp(_hand: str, _object: str, _force: float) -> bool:
    """Placeholder for Task 3 grasping."""
    raise NotImplementedError


def coordinate_bimanual(_plan: Plan) -> tuple[JointState, ...]:
    """Placeholder for Task 4 bimanual coordination."""
    raise NotImplementedError


def create_plan(_voice_request: str, _scene: dict[str, object]) -> Plan:
    """Placeholder for Task 5 LLM or hard-coded planning."""
    raise NotImplementedError
