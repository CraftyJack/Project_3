score_model_features = [ 
'state',
'county',
'tract',
'block_group',
'flag',
'land_area',
'aian_land',
'urbanized_area_pop_cen_2010',
'urban_cluster_pop_cen_2010',
'rural_pop_cen_2010',
'tot_population_cen_2010',
'tot_population_acs_09_13',
'males_cen_2010',
'males_acs_09_13',
'females_cen_2010',
'females_acs_09_13',
'pop_under_5_cen_2010',
'pop_under_5_acs_09_13',
'pop_5_17_cen_2010',
'pop_5_17_acs_09_13',
'pop_18_24_cen_2010',
'pop_18_24_acs_09_13',
'pop_25_44_cen_2010',
'pop_25_44_acs_09_13',
'pop_45_64_cen_2010',
'pop_45_64_acs_09_13',
'pop_65plus_cen_2010',
'pop_65plus_acs_09_13',
'tot_gq_cen_2010',
'inst_gq_cen_2010',
'non_inst_gq_cen_2010',
'hispanic_cen_2010',
'hispanic_acs_09_13',
'nh_white_alone_cen_2010',
'nh_white_alone_acs_09_13',
'nh_blk_alone_cen_2010',
'nh_blk_alone_acs_09_13',
'nh_aian_alone_cen_2010',
'nh_aian_alone_acs_09_13',
'nh_asian_alone_cen_2010',
'nh_asian_alone_acs_09_13',
'nh_nhopi_alone_cen_2010',
'nh_nhopi_alone_acs_09_13',
'nh_sor_alone_cen_2010',
'nh_sor_alone_acs_09_13',
'pop_5yrs_over_acs_09_13',
'othr_lang_acs_09_13',
'pop_25yrs_over_acs_09_13',
'not_hs_grad_acs_09_13',
'college_acs_09_13',
'pov_univ_acs_09_13',
'prs_blw_pov_lev_acs_09_13',
'one_health_ins_acs_09_13',
'two_plus_health_ins_acs_09_13',
'no_health_ins_acs_09_13',
'pop_1yr_over_acs_09_13',
'diff_hu_1yr_ago_acs_09_13',
'eng_vw_span_acs_09_13',
'eng_vw_indo_euro_acs_09_13',
'eng_vw_api_acs_09_13',
'eng_vw_other_acs_09_13',
'eng_vw_acs_09_13',
'rel_family_hhds_cen_2010',
'rel_family_hhd_acs_09_13',
'mrdcple_fmly_hhd_cen_2010',
'mrdcple_fmly_hhd_acs_09_13',
'not_mrdcple_hhd_cen_2010',
'not_mrdcple_hhd_acs_09_13',
'female_no_hb_cen_2010',
'female_no_hb_acs_09_13',
'nonfamily_hhd_cen_2010',
'nonfamily_hhd_acs_09_13',
'sngl_prns_hhd_cen_2010',
'sngl_prns_hhd_acs_09_13',
'hhd_ppl_und_18_cen_2010',
'hhd_ppl_und_18_acs_09_13',
'tot_prns_in_hhd_cen_2010',
'tot_prns_in_hhd_acs_09_13',
'rel_child_under_6_cen_2010',
'rel_child_under_6_acs_09_13',
'hhd_moved_in_acs_09_13',
'pub_asst_inc_acs_09_13',
'med_hhd_inc_bg_acs_09_13',
'med_hhd_inc_tr_acs_09_13',
'aggregate_hh_inc_acs_09_13',
'tot_housing_units_cen_2010',
'tot_housing_units_acs_09_13',
'tot_occp_units_cen_2010',
'tot_occp_units_acs_09_13',
'tot_vacant_units_cen_2010',
'tot_vacant_units_acs_09_13',
'renter_occp_hu_cen_2010',
'renter_occp_hu_acs_09_13',
'owner_occp_hu_cen_2010',
'owner_occp_hu_acs_09_13',
'single_unit_acs_09_13',
'mlt_u2_9_strc_acs_09_13',
'mlt_u10p_acs_09_13',
'mobile_homes_acs_09_13',
'crowd_occp_u_acs_09_13',
'occp_u_no_ph_srvc_acs_09_13',
'no_plumb_acs_09_13',
'recent_built_hu_acs_09_13',
'med_house_value_bg_acs_09_13',
'med_house_value_tr_acs_09_13',
'aggr_house_value_acs_09_13',
'mailback_area_count_cen_2010',
'tea_mail_out_mail_back_cen_2010',
'tea_update_leave_cen_2010',
'census_mail_returns_cen_2010',
'vacants_cen_2010',
'deletes_cen_2010',
'census_uaa_cen_2010',
'valid_mailback_count_cen_2010',
'frst_frms_cen_2010',
'rplcmnt_frms_cen_2010',
'bilq_mailout_count_cen_2010',
'bilq_frms_cen_2010',
'mail_return_rate_cen_2010',
'low_response_score',
'pct_urbanized_area_pop_cen_2010',
'pct_urban_cluster_pop_cen_2010',
'pct_rural_pop_cen_2010',
'pct_males_cen_2010',
'pct_males_acs_09_13',
'pct_females_cen_2010',
'pct_females_acs_09_13',
'pct_pop_under_5_cen_2010',
'pct_pop_under_5_acs_09_13',
'pct_pop_5_17_cen_2010',
'pct_pop_5_17_acs_09_13',
'pct_pop_18_24_cen_2010',
'pct_pop_18_24_acs_09_13',
'pct_pop_25_44_cen_2010',
'pct_pop_25_44_acs_09_13',
'pct_pop_45_64_cen_2010',
'pct_pop_45_64_acs_09_13',
'pct_pop_65plus_cen_2010',
'pct_pop_65plus_acs_09_13',
'pct_tot_gq_cen_2010',
'pct_inst_gq_cen_2010',
'pct_non_inst_gq_cen_2010',
'pct_hispanic_cen_2010',
'pct_hispanic_acs_09_13',
'pct_nh_white_alone_cen_2010',
'pct_nh_white_alone_acs_09_13',
'pct_nh_blk_alone_cen_2010',
'pct_nh_blk_alone_acs_09_13',
'pct_nh_aian_alone_cen_2010',
'pct_nh_aian_alone_acs_09_13',
'pct_nh_asian_alone_cen_2010',
'pct_nh_asian_alone_acs_09_13',
'pct_nh_nhopi_alone_cen_2010',
'pct_nh_nhopi_alone_acs_09_13',
'pct_nh_sor_alone_cen_2010',
'pct_nh_sor_alone_acs_09_13',
'pct_pop_5yrs_over_acs_09_13',
'pct_othr_lang_acs_09_13',
'pct_pop_25yrs_over_acs_09_13',
'pct_not_hs_grad_acs_09_13',
'pct_college_acs_09_13',
'pct_prs_blw_pov_lev_acs_09_13',
'pct_one_health_ins_acs_09_13',
'pct_twophealth_ins_acs_09_13',
'pct_no_health_ins_acs_09_13',
'pct_pov_univ_acs_09_13',
'pct_pop_1yr_over_acs_09_13',
'pct_diff_hu_1yr_ago_acs_09_13',
'pct_eng_vw_span_acs_09_13',
'pct_eng_vw_indoeuro_acs_09_13',
'pct_eng_vw_api_acs_09_13',
'pct_eng_vw_other_acs_09_13',
'pct_eng_vw_acs_09_13',
'pct_rel_family_hhds_cen_2010',
'pct_rel_family_hhd_acs_09_13',
'pct_mrdcple_hhd_cen_2010',
'pct_mrdcple_hhd_acs_09_13',
'pct_not_mrdcple_hhd_cen_2010',
'pct_not_mrdcple_hhd_acs_09_13',
'pct_female_no_hb_cen_2010',
'pct_female_no_hb_acs_09_13',
'pct_nonfamily_hhd_cen_2010',
'pct_nonfamily_hhd_acs_09_13',
'pct_sngl_prns_hhd_cen_2010',
'pct_sngl_prns_hhd_acs_09_13',
'pct_hhd_ppl_und_18_cen_2010',
'pct_hhd_ppl_und_18_acs_09_13',
'avg_tot_prns_in_hhd_cen_2010',
'avg_tot_prns_in_hhd_acs_09_13',
'pct_rel_under_6_cen_2010',
'pct_rel_under_6_acs_09_13',
'pct_hhd_moved_in_acs_09_13',
'pct_pub_asst_inc_acs_09_13',
'avg_agg_hh_inc_acs_09_13',
'pct_tot_occp_units_cen_2010',
'pct_tot_occp_units_acs_09_13',
'pct_vacant_units_cen_2010',
'pct_vacant_units_acs_09_13',
'pct_renter_occp_hu_cen_2010',
'pct_renter_occp_hu_acs_09_13',
'pct_owner_occp_hu_cen_2010',
'pct_owner_occp_hu_acs_09_13',
'pct_single_unit_acs_09_13',
'pct_mlt_u2_9_strc_acs_09_13',
'pct_mlt_u10p_acs_09_13',
'pct_mobile_homes_acs_09_13',
'pct_crowd_occp_u_acs_09_13',
'pct_no_ph_srvc_acs_09_13',
'pct_no_plumb_acs_09_13',
'pct_recent_built_hu_acs_09_13',
'avg_agg_house_value_acs_09_13',
'pct_tea_mailoutmailback_cen_2010',
'pct_tea_update_leave_cen_2010',
'pct_census_mail_returns_cen_2010',
'pct_vacant_cen_2010',
'pct_deletes_cen_2010',
'pct_census_uaa_cen_2010',
'pct_mailback_count_cen_2010',
'pct_frst_frms_cen_2010',
'pct_rplcmnt_frms_cen_2010',
'pct_bilq_mailout_count_cen_2010'
]
site_model_features = [ 
'land_area',
'rural_pop_cen_2010',
'mlt_u2_9_strc_acs_09_13',
'med_house_value_bg_acs_09_13',
'med_house_value_tr_acs_09_13',
'mail_return_rate_cen_2010',
'low_response_score',
'pct_urbanized_area_pop_cen_2010',
'pct_rural_pop_cen_2010',
'pct_males_cen_2010',
'pct_males_acs_09_13',
'pct_females_cen_2010',
'pct_females_acs_09_13',
'pct_pop_18_24_cen_2010',
'pct_pop_18_24_acs_09_13',
'pct_pop_25_44_cen_2010',
'pct_pop_45_64_cen_2010',
'pct_pop_65plus_cen_2010',
'pct_pop_65plus_acs_09_13',
'pct_hispanic_cen_2010',
'pct_nh_white_alone_cen_2010',
'pct_not_hs_grad_acs_09_13',
'pct_college_acs_09_13',
'pct_one_health_ins_acs_09_13',
'pct_sngl_prns_hhd_acs_09_13',
'pct_owner_occp_hu_cen_2010',
'pct_single_unit_acs_09_13',
'pct_mlt_u2_9_strc_acs_09_13',
'pct_census_uaa_cen_2010',
'pct_mailback_count_cen_2010'
]
