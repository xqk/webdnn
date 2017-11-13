from webdnn.backend.webgl.optimize_rules import attach_concat_workspace
from webdnn.backend.webgl.optimize_rules import decompose_softmax
from webdnn.backend.webgl.optimize_rules import fix_sgemm_texture_shape
from webdnn.backend.webgl.optimize_rules import fix_tensordot_texture_shape
from webdnn.backend.webgl.optimize_rules import insert_channel_mode_conversion
from webdnn.backend.webgl.optimize_rules import insert_transpose
from webdnn.backend.webgl.optimize_rules import replace_tensordot_by_sgemm
from webdnn.backend.webgl.optimize_rules import simplify_channel_mode_conversion
from webdnn.backend.webgl.optimize_rules import split_texture
from webdnn.backend.webgl.optimize_rules import webgl_optimize_rule
