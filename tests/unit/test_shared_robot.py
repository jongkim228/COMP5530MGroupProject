import mujoco


def test_shared_model_loads(robot_model: mujoco.MjModel) -> None:
    assert robot_model.nbody > 0
    assert robot_model.nq > 0


def test_shared_model_starts_deterministically(
    robot_model: mujoco.MjModel,
    robot_data: mujoco.MjData,
) -> None:
    mujoco.mj_forward(robot_model, robot_data)
    assert robot_data.time == 0.0
