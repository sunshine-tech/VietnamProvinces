================
VietnamProvinces
================

|image love| |image pypi|

[`Tiếng Việt <vietnamese_>`_]

Library to provide list of Vietnam administrative divisions (tỉnh thành, quận huyện, phường xã) with the name and code as defined by `General Statistics Office of Viet Nam <gso_vn_>`_ (Tổng cục Thống kê).

Example:

.. code-block:: json

    {
        "name": "Tỉnh Cà Mau",
        "code": 96,
        "codename": "tinh_ca_mau",
        "division_type": "tỉnh",
        "phone_code": 290,
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

This library provides data in these forms:

1. JSON

This data is suitable for applications which don't need to access the data often. They are fine with loading JSON and extract information from it. The JSON files are saved in *data* folder. You can get the file path via ``vietnam_provinces.NESTED_DIVISIONS_JSON_PATH`` variable.

Note that this variable only returns the path of the file, not the content. It is up to application developer to use any method to parse the JSON. For example:

.. code-block:: python

    import orjson
    import rapidjson
    from vietnam_provinces import NESTED_DIVISIONS_JSON_PATH

    # With rapidjson
    with NESTED_DIVISIONS_JSON_PATH.open() as f:
        rapidjson.load(f)

    # With orjson
    orjson.loads(NESTED_DIVISIONS_JSON_PATH.read_bytes())

Due to the big amount of data (10609 wards all over Viet Nam), this loading will be slow.


2. Python data type

This data is useful for some applications which need to access the data more often. They are built as ``Enum``, where you can import in Python code:

.. code-block:: python

    >>> from vietnam_provinces.enums import ProvinceEnum, ProvinceDEnum, DistrictEnum, DistrictDEnum

    >>> ProvinceEnum.P_77
    <ProvinceEnum.P_77: Province(name='Tỉnh Bà Rịa - Vũng Tàu', code=77, division_type=<VietNamDivisionType.TINH: 'tỉnh'>, codename='tinh_ba_ria_vung_tau', phone_code=254)>

    >>> ProvinceDEnum.BA_RIA_VUNG_TAU
    <ProvinceDEnum.BA_RIA_VUNG_TAU: Province(name='Tỉnh Bà Rịa - Vũng Tàu', code=77, division_type=<VietNamDivisionType.TINH: 'tỉnh'>, codename='tinh_ba_ria_vung_tau', phone_code=254)>

    >>> DistrictEnum.D_624
    >>> <DistrictEnum.D_624: District(name='Thị xã Ayun Pa', code=624, division_type=<VietNamDivisionType.THI_XA: 'thị xã'>, codename='thi_xa_ayun_pa', province_code=64)>

    >>> DistrictDEnum.AYUN_PA_GL
    <DistrictDEnum.AYUN_PA_GL: District(name='Thị xã Ayun Pa', code=624, division_type=<VietNamDivisionType.THI_XA: 'thị xã'>, codename='thi_xa_ayun_pa', province_code=64)>

    >>> from vietnam_provinces.enums.wards import WardEnum, WardDEnum

    >>> WardEnum.W_7450
    <WardEnum.W_7450: Ward(name='Xã Đông Hưng', code=7450, division_type=<VietNamDivisionType.XA: 'xã'>, codename='xa_dong_hung', district_code=218)>

    >>> WardDEnum.BG_DONG_HUNG_7450
    <WardDEnum.BG_DONG_HUNG_7450: Ward(name='Xã Đông Hưng', code=7450, division_type=<VietNamDivisionType.XA: 'xã'>, codename='xa_dong_hung', district_code=218)>


Loading wards this way is far more faster than the JSON option.

They are made as ``Enum``, so that library user can take advantage of auto-complete feature of IDE/code editors in development. It prevents typo mistake.

The Ward Enum has two variants:

- ``WardEnum``: Has member name in form of numeric ward code (``W_28912``). It helps look up a ward by its code (which is a most-seen use case).

- ``WardDEnum``: Has more readable member name (``D`` means "descriptive"), to help the application code easier to reason about. For example, looking at ``WardDEnum.BT_PHAN_RI_CUA_22972``, the programmer can guess that this ward is "Phan Rí Cửa", of "Bình Thuận" province.

Similarly, other levels (District, Province) also have two variants of Enum.

Example of looking up ``Ward``, ``District``, ``Province`` with theirs numeric code:

.. code-block:: python

    # Assume that you are loading user info from your database
    user_info = load_user_info()

    province_code = user_info['province_code']
    province = ProvinceEnum[f'P_{province_code}'].value

Unlike ``ProvinceDEnum``, ``DistrictDEnum``, the ``WardDEnum`` has ward code in member name. It is because there are too many Vietnamese wards with the same name. There is no way to build unique ID for wards, with pure Latin letters (Vietnamese punctuations stripped), even if we add district and province info to the ID. Let's take "Xã Đông Thành" and "Xã Đông Thạnh" as example. Both belong to "Huyện Bình Minh" of "Vĩnh Long", both produces ID name "DONG_THANH". Although Python allows Unicode as ID name, like "ĐÔNG_THẠNH", but it is not practical yet because the code formatter tool (`Black`_) will still normalizes it to Latin form.

Because the ``WardEnum`` has many records (10609 in February 2021) and may not be needed in some applications, I move it to separate module, to avoid loading automatically to application.


Member of these enums, the ``Province``, ``District`` and ``Ward`` data types, can be imported from top-level of ``vietnam_provinces``.

.. code-block:: python

    >>> from vietnam_provinces import Province, District, Ward


Install
-------

.. code-block:: sh

    pip3 install vietnam-provinces


This library is compatible with Python 3.7+.


Development
-----------

In development, this project has a tool to convert data from government sources.

The tool doesn't directly crawl data from government websites because the data rarely change (it doesn't worth developing the feature which you only need to use each ten years), and because those websites provide data in unfriendly Microsoft Office formats.

The tool is tested on Linux only (may not run on Windows).

Update data
~~~~~~~~~~~

In the future, when the authority reorganize administrative divisions, we need to collect this data again from GSOVN website. Do:

- Go to: https://danhmuchanhchinh.gso.gov.vn/ (this URL may change when `GSOVN <gso_vn_>`_ replaces their software).
- Find the button "Xuất Excel".
- Tick the "Quận Huyện Phường Xã" checkbox.
- Click the button to export and download list of units in Excel (XLS) file.
- Use LibreOffice to convert Excel file to CSV file. For example, we name it *Xa_2023-05-07.csv*.
- Run this tool to compute data to JSON format:

.. code-block:: sh

    python3 -m dev -i dev/seed-data/Xa_2023-05-07.csv -o vietnam_provinces/data/nested-divisions.json

You can run

.. code-block:: sh

    python3 -m dev --help

to see more options of that tool.

Note that this tool is only available in the source folder (cloned from Git). It is not included in the distributable Python package.


Generate Python code
~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh

    python3 -m dev -i dev/seed-data/Xa_2023-05-07.csv -f python


Data source
~~~~~~~~~~~

- Name and code of provinces, districts and wards:  `General Statistics Office of Viet Nam <gso_vn_>`_.
- Phone area code: `Thái Bình province's department of Information and Communication <tb_ic_>`_.


Credit
------

Given to you by `Nguyễn Hồng Quân <quan_>`_, after nights and weekends.


.. |image love| image:: https://madewithlove.now.sh/vn?heart=true&colorA=%23ffcd00&colorB=%23da251d
.. |image pypi| image:: https://badgen.net/pypi/v/vietnam-provinces
   :target: https://pypi.org/project/vietnam-provinces/
.. _vietnamese: README.vi_VN.rst
.. _gso_vn: https://www.gso.gov.vn/
.. _tb_ic: https://sotttt.thaibinh.gov.vn/tin-tuc/buu-chinh-vien-thong/tra-cuu-ma-vung-dien-thoai-co-dinh-mat-dat-ma-mang-dien-thoa2.html
.. _dataclass: https://docs.python.org/3/library/dataclasses.html
.. _fast-enum: https://pypi.org/project/fast-enum/
.. _pydantic: https://pypi.org/project/pydantic/
.. _Black: https://github.com/psf/black
.. _quan: https://quan.hoabinh.vn
