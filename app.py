import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
rds_connection_string = "postgres:postgres@localhost:5432/project_2_db"
engine = create_engine(f'postgresql://{rds_connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
superfund_sites = Base.classes.superfund_analysis_table

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/all_data<br/>"
        f"/api/v1.0/state_list"
    )


@app.route("/api/v1.0/all_data")
def all_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all site data"""
    # Query all site data
    results = session.query(superfund_sites.id, superfund_sites.address,\
                            superfund_sites.city, superfund_sites.latitude,\
                            superfund_sites.longitude, superfund_sites.site_score,\
                            superfund_sites.state_name, superfund_sites.county_name,\
                            superfund_sites.tract, superfund_sites.block_group,\
                            superfund_sites.tot_population_cen_2010, superfund_sites.hispanic_cen_2010,\
                            superfund_sites.nh_blk_alone_cen_2010, superfund_sites.nh_aian_alone_cen_2010,\
                            superfund_sites.nh_asian_alone_cen_2010, superfund_sites.nh_nhopi_alone_cen_2010,\
                            superfund_sites.nh_sor_alone_cen_2010, superfund_sites.college_acs_09_13,\
                            superfund_sites.no_health_ins_acs_09_13, superfund_sites.med_hhd_inc_bg_acs_09_13,\
                            superfund_sites.aggregate_hh_inc_acs_09_13, superfund_sites.tot_vacant_units_cen_2010,\
                            superfund_sites.renter_occp_hu_cen_2010, superfund_sites.owner_occp_hu_cen_2010,\
                            superfund_sites.no_plumb_acs_09_13, superfund_sites.med_house_value_bg_acs_09_13,\
                            superfund_sites.pct_hispanic_cen_2010, superfund_sites.pct_nh_blk_alone_cen_2010,\
                            superfund_sites.pct_nh_aian_alone_cen_2010, superfund_sites.pct_nh_asian_alone_cen_2010,\
                            superfund_sites.pct_nh_nhopi_alone_cen_2010, superfund_sites.pct_nh_sor_alone_cen_2010,\
                            superfund_sites.pct_not_hs_grad_acs_09_13, superfund_sites.pct_no_health_ins_acs_09_13,\
                            superfund_sites.pct_vacant_units_cen_2010, superfund_sites.pct_renter_occp_hu_cen_2010,\
                            superfund_sites.pct_owner_occp_hu_cen_2010, superfund_sites.pct_no_plumb_acs_09_13,\
                            superfund_sites.pct_poc).all()

    session.close()

    # Create a dictionary from the row data and append to a list of site data
    site_data = []
    for id, address, city, latitude, longitude, site_score, state_name, county_name, tract, block_group,\
        tot_population_cen_2010,hispanic_cen_2010, nh_blk_alone_cen_2010, nh_aian_alone_cen_2010,\
        nh_asian_alone_cen_2010, nh_nhopi_alone_cen_2010, nh_sor_alone_cen_2010, college_acs_09_13,\
        no_health_ins_acs_09_13, med_hhd_inc_bg_acs_09_13, aggregate_hh_inc_acs_09_13, tot_vacant_units_cen_2010,\
        renter_occp_hu_cen_2010, owner_occp_hu_cen_2010, no_plumb_acs_09_13, med_house_value_bg_acs_09_13,\
        pct_hispanic_cen_2010, pct_nh_blk_alone_cen_2010, pct_nh_aian_alone_cen_2010, pct_nh_asian_alone_cen_2010,\
        pct_nh_nhopi_alone_cen_2010, pct_nh_sor_alone_cen_2010, pct_not_hs_grad_acs_09_13, pct_no_health_ins_acs_09_13,\
        pct_vacant_units_cen_2010, pct_renter_occp_hu_cen_2010, pct_owner_occp_hu_cen_2010, pct_no_plumb_acs_09_13,\
        pct_poc in results:
        site_data_dict = {}
        site_data_dict["id"] = id
        site_data_dict["address"] = address
        site_data_dict["city"] = city
        site_data_dict["latitude"] = latitude
        site_data_dict["longitude"] = longitude
        site_data_dict["site_score"] = site_score
        site_data_dict["state_name"] = state_name
        site_data_dict["county_name"] = county_name
        site_data_dict["tract"] = tract
        site_data_dict["block_group"] = block_group
        site_data_dict["tot_population_cen_2010"] = tot_population_cen_2010
        site_data_dict["hispanic_cen_2010"] = hispanic_cen_2010
        site_data_dict["nh_blk_alone_cen_2010"] = nh_blk_alone_cen_2010
        site_data_dict["nh_aian_alone_cen_2010"] = nh_aian_alone_cen_2010
        site_data_dict["nh_asian_alone_cen_2010"] = nh_asian_alone_cen_2010
        site_data_dict["nh_nhopi_alone_cen_2010"] = nh_nhopi_alone_cen_2010
        site_data_dict["nh_sor_alone_cen_2010"] = nh_sor_alone_cen_2010
        site_data_dict["college_acs_09_13"] = college_acs_09_13
        site_data_dict["no_health_ins_acs_09_13"] = no_health_ins_acs_09_13
        site_data_dict["med_hhd_inc_bg_acs_09_13"] = med_hhd_inc_bg_acs_09_13
        site_data_dict["aggregate_hh_inc_acs_09_13"] = aggregate_hh_inc_acs_09_13
        site_data_dict["tot_vacant_units_cen_2010"] = tot_vacant_units_cen_2010
        site_data_dict["renter_occp_hu_cen_2010"] = renter_occp_hu_cen_2010
        site_data_dict["owner_occp_hu_cen_2010"] = owner_occp_hu_cen_2010
        site_data_dict["no_plumb_acs_09_13"] = no_plumb_acs_09_13
        site_data_dict["med_house_value_bg_acs_09_13"] = med_house_value_bg_acs_09_13
        site_data_dict["pct_hispanic_cen_2010"] = pct_hispanic_cen_2010
        site_data_dict["pct_nh_blk_alone_cen_2010"] = pct_nh_blk_alone_cen_2010
        site_data_dict["pct_nh_aian_alone_cen_2010"] = pct_nh_aian_alone_cen_2010
        site_data_dict["pct_nh_asian_alone_cen_2010"] = pct_nh_asian_alone_cen_2010
        site_data_dict["pct_nh_nhopi_alone_cen_2010"] = pct_nh_nhopi_alone_cen_2010
        site_data_dict["pct_nh_sor_alone_cen_2010"] = pct_nh_sor_alone_cen_2010
        site_data_dict["pct_not_hs_grad_acs_09_13"] = pct_not_hs_grad_acs_09_13
        site_data_dict["pct_no_health_ins_acs_09_13"] = pct_no_health_ins_acs_09_13
        site_data_dict["pct_vacant_units_cen_2010"] = pct_vacant_units_cen_2010
        site_data_dict["pct_renter_occp_hu_cen_2010"] = pct_renter_occp_hu_cen_2010
        site_data_dict["pct_owner_occp_hu_cen_2010"] = pct_owner_occp_hu_cen_2010
        site_data_dict["pct_no_plumb_acs_09_13"] = pct_no_plumb_acs_09_13
        site_data_dict["pct_poc"] = pct_poc
        site_data.append(site_data_dict)

    return jsonify(site_data)

@app.route("/api/v1.0/state_list")
def state_list():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Return a list of state names"""
    results = session.query(superfund_sites.state_name).distinct().order_by(superfund_sites.state_name).all()
        
    """Remove first entry for readability"""
    results.pop(0)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)