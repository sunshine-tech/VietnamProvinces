================
VietnamProvinces
================


Library to provide list of Vietnam administrative divisions (tỉnh thành, quận huyện, phường xã) with the name and code as defined by `General Statistics Office of Viet Nam <gso_vn_>`_ (Tổng cục Thống kê).

Example:

.. code-block:: json

    {
        "name": "Tỉnh Cà Mau",
        "code": 96,
        "codename": "tinh_ca_mau",
        "division_type": "tỉnh",
        "districts": [
            {
                "name": "Huyện Đầm Dơi",
                "code": 970,
                "codename": "huyen_dam_doi",
                "division_type": "huyện",
                "wards": [
                {
                    "name": "Thị trấn Đầm Dơi",
                    "code": 32152,
                    "codename": "thi_tran_dam_doi",
                    "division_type": "thị trấn"
                },
                {
                    "name": "Xã Tạ An Khương",
                    "code": 32155,
                    "codename": "xa_ta_an_khuong",
                    "division_type": "xã"
                },
                ]
            }
        ]
    }


Development
-----------

Currently, this project is making tool to crawl `GSO <gso_vn_>`_ data. It doesnot provide library as planned yet.

Update data
~~~~~~~~~~~

This data is not static. In the future, when the authority reorganize administrative divisions, we need to crawl this data again from GSOVN website. Do:

- Go to: https://www.gso.gov.vn/dmhc2015/ (this URL may change when `GSOVN <gso_vn_>`_ replaces their software).
- Find the button "Xuất Excel".
- Tick the "Quận Huyện Phường Xã" checkbox.
- Click the button to export and download list of units in Excel (XLS) file.
- Use LibreOffice to convert Excel file to CSV file. For example, we name it *Xa_2020-02-25.csv*.
- Run this tool to compute data to JSON format:

    .. code-block:: sh

        python3 -m vietnam_provinces.tools -i ../Data/Xa_2020-02-25.csv -f nested-json -o ../Data/nested.json

.. _gso_vn: https://www.gso.gov.vn/
