try:
    from main import get_data, run_suma, neuro_to_radio, pre_slice, pre_volreg, pre_scale, vol_to_surf, surf_to_vol, surf_smooth, roi_templates, subset_rois, roi_get_data, roi_subjects, roi_group, whole_group, fft_analysis, hotelling_t2, fit_error_ellipse, read, write
    from utils import bids_organizer, hard_create
except ImportError:
    from .main import get_data, run_suma, neuro_to_radio, pre_slice, pre_volreg, pre_scale, vol_to_surf, surf_to_vol, surf_smooth, roi_templates, subset_rois, roi_get_data, roi_subjects, roi_group, whole_group, fft_analysis, hotelling_t2, fit_error_ellipse, read, write
    from .utils import bids_organizer, hard_create

