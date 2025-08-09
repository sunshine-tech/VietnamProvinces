================
VietnamProvinces
================

|image love| |image pypi| |common changelog|

[`Tiếng Việt <vietnamese_>`_]

Library to provide list of Vietnam administrative divisions (tỉnh thành, phường xã, after the rearrangement in July 2025) with the name and code as defined by `Draft of new administrative units <draft_new_units_>`_ (Tổng cục Thống kê).

Example:

.. code-block:: json

  {
    "name": "Tuyên Quang",
    "code": 8,
    "codename": "tuyen_quang",
    "division_type": "tỉnh",
    "phone_code": 207,
    "wards": [
      {
        "name": "Xã Thượng Lâm",
        "code": 2269,
        "codename": "xa_thuong_lam",
        "division_type": "xã",
        "short_codename": "thuong_lam"
      },
      {
        "name": "Xã Lâm Bình",
        "code": 2266,
        "codename": "xa_lam_binh",
        "division_type": "xã",
        "short_codename": "lam_binh"
      },
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


2. Python data type

This data is useful for some applications which need to access the data more often.
There are two kinds of objects, first is the object presenting a single province or ward, second is province code or ward code in form of `enum`, which you can import in Python code:

.. code-block:: python

    >>> from vietnam_provinces import ProvinceCode, Province, WardCode, Ward

    >>> Province.from_code(ProvinceCode.P_15)
    Province(name='Lào Cai', code=<ProvinceCode.P_15: 15>, division_type=<VietNamDivisionType.TINH: 'tỉnh'>, codename='lao_cai', phone_code=214)

    >>> Ward.from_code(23425)
    Ward(name='Xã Tu Mơ Rông', code=<WardCode.W_23425: 23425>, division_type=<VietNamDivisionType.XA: 'xã'>, codename='xa_tu_mo_rong', province_code=<ProvinceCode.P_51: 51>)


To know if the data is up-to-date, check the ``__data_version__`` attribute of the module:

.. code-block:: python

    >>> import vietnam_provinces
    >>> vietnam_provinces.__data_version__
    '2025-08-02'


Install
-------

.. code-block:: sh

    python -m pip install vietnam-provinces
    # or
    uv add vietnam-provinces


This library is compatible with Python 3.10+.


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
- Use LibreOffice to convert Excel file to CSV file. For example, we name it *Xa_2025-01-04.csv*.
- Run this tool to compute data to JSON format:

.. code-block:: sh

    python3 -m dev -w dev/seed-data/2025-07/Cap-xa.csv -p dev/seed-data/2025-07/Cap-tinh.csv -f nested-json

You can run

.. code-block:: sh

    python3 -m dev --help

to see more options of that tool.

Note that this tool is only available in the source folder (cloned from Git). It is not included in the distributable Python package.


Generate Python code
~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh

    python3 -m dev -w dev/seed-data/2025-07/Cap-xa.csv -p dev/seed-data/2025-07/Cap-tinh.csv -f python


Data source
~~~~~~~~~~~

- Name and code of provinces, and wards:  `General Statistics Office of Viet Nam <gso_vn_>`_.
- Phone area code: `Thái Bình province's department of Information and Communication <tb_ic_>`_.


Credit
------

Given to you by `Nguyễn Hồng Quân <quan_>`_, after nights and weekends.


.. |image love| image:: https://madewithlove.now.sh/vn?heart=true&colorA=%23ffcd00&colorB=%23da251d
.. |image pypi| image:: https://badgen.net/pypi/v/vietnam-provinces
   :target: https://pypi.org/project/vietnam-provinces/
.. |common changelog| image:: https://common-changelog.org/badge.svg
   :target: https://common-changelog.org
.. _vietnamese: README.vi_VN.rst
.. _gso_vn: https://danhmuchanhchinh.gso.gov.vn/
.. _draft_new_units: https://chinhphu.vn/du-thao-vbqppl/du-thao-quyet-dinh-cua-thu-tuong-chinh-phu-ban-hanh-bang-danh-muc-va-ma-so-cac-don-vi-hanh-chinh-7546
.. _tb_ic: https://sotttt.thaibinh.gov.vn/tin-tuc/buu-chinh-vien-thong/tra-cuu-ma-vung-dien-thoai-co-dinh-mat-dat-ma-mang-dien-thoa2.html
.. _dataclass: https://docs.python.org/3/library/dataclasses.html
.. _pydantic: https://pypi.org/project/pydantic/
.. _quan: https://quan.hoabinh.vn
