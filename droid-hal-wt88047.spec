# These and other macros are documented in dhd/droid-hal-device.inc
%define device wt88047
%define vendor wingtech
%define vendor_pretty Xiaomi
%define device_pretty Redmi2
%define installable_zip 1

# Entries migrated from the old rpm/droid-hal-z3c.spec for qcom-bsp 
%define android_config \
#define QCOM_BSP 1\
%{nil}

# Add nemo to correct groups 
%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
/usr/bin/groupadd-user inet || :\
%{nil}

# Straggler files below
%define straggler_files \
/init.qti.ims.sh\
/selinux_version\
/service_contexts\
%{nil}
%include rpm/dhd/droid-hal-device.inc

