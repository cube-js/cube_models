from models import Cube, Dimension, Measure

orders = Cube(
    name='orders',
    dimensions=(
        Dimension(name="creation_timestamp", type="timestamp", sql="dateCreated"),
        Dimension(name="user_id", type="number", sql="dateCreated"),
    ),
    measures=(
        Measure(name="count", type="count"),
    )
)