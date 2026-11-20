from pathlib import Path

import mujoco
import pytest


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def robot_model() -> mujoco.MjModel:
    return mujoco.MjModel.from_xml_path(str(ROOT / "models" / "robot.xml"))


@pytest.fixture
def robot_data(robot_model: mujoco.MjModel) -> mujoco.MjData:
    return mujoco.MjData(robot_model)
