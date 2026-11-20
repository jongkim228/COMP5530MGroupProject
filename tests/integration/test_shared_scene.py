from pathlib import Path

import mujoco
import pytest


@pytest.mark.integration
def test_shared_scene_loads() -> None:
    scene = Path(__file__).resolve().parents[2] / "models" / "scenes" / "shared.xml"
    model = mujoco.MjModel.from_xml_path(str(scene))
    data = mujoco.MjData(model)
    for _ in range(10):
        mujoco.mj_step(model, data)
