from collections.abc import Sequence

import numpy as np

from .transforms import BboxBase

def affine_transform(points: np.ndarray, trans: np.ndarray) -> np.ndarray: ...
def count_bboxes_overlapping_bbox(bbox: BboxBase, bboxes: Sequence[BboxBase]) -> int: ...
def update_path_extents(path, trans, rect, minpos, ignore): ...
