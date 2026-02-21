================
VietnamProvinces
================

|image love| |image pypi| |common changelog|

[`Tiếng Việt <vietnamese_>`_]

Library to provide list of Vietnam administrative divisions (tỉnh thành, phường xã, after the rearrangement in July 2025) with the name and code as defined by `National Statistics Office of Viet Nam <nso_vn_>`_.

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
    Province(name='Tỉnh Lào Cai', code=<ProvinceCode.P_15: 15>, division_type=<VietNamDivisionType.TINH: 'tỉnh'>, codename='lao_cai', phone_code=214)

    >>> Ward.from_code(23425)
    Ward(name='Xã Tu Mơ Rông', code=<WardCode.W_23425: 23425>, division_type=<VietNamDivisionType.XA: 'xã'>, codename='xa_tu_mo_rong', province_code=<ProvinceCode.P_51: 51>)

    >>> # Search provinces by name
    >>> Province.search('lao cai')
    (Province(name='Tỉnh Lào Cai', ...),)

    >>> # Search wards by name
    >>> Ward.search('phu my')
    (Ward(name='Phường Phú Mỹ', ...), Ward(name='Xã Phú Mỹ', ...), ...)

    >>> # Search current wards by legacy data (pre-2025)
    >>> Ward.search_from_legacy(name='phu my')
    (WardWithLegacy(source_code=21730, ward=Ward(name='Xã Phù Mỹ', ...)), ...)

    >>> # Get legacy wards that were merged to form a new ward
    >>> ward = Ward.from_code(4)  # Phường Ba Đình
    >>> ward.get_legacy_sources()
    (Ward(name='Phường Trúc Bạch', ...), Ward(name='Phường Quán Thánh', ...), ...)

    >>> # Search current wards by legacy district (districts were dissolved in 2025)
    >>> Ward.search_from_legacy_district(code=748)  # Thành phố Bà Rịa (old)
    (WardWithLegacy(source_code=26710, ward=Ward(name='Phường Bà Rịa', ...)), ...)

    >>> # Search current provinces by legacy province code (pre-2025)
    >>> Province.search_from_legacy(code=77)  # Tỉnh Bà Rịa - Vũng Tàu
    (ProvinceWithLegacy(source_code=77, province=Province(name='Thành phố Hồ Chí Minh', ...)),)

    >>> # Get legacy provinces that were merged to form a new province
    >>> province = Province.from_code(79)  # Thành phố Hồ Chí Minh
    >>> province.get_legacy_sources()
    (Province(name='Tỉnh Bình Dương', ...), Province(name='Tỉnh Bà Rịa - Vũng Tàu', ...), Province(name='Thành phố Hồ Chí Minh', ...))

The pre-2025 data types can then be used as:

.. code-block:: python

    from vietnam_provinces.legacy import Province, District, Ward
    from vietnam_provinces.legacy.codes import ProvinceCode

    # Look up by code
    province = Province.from_code(ProvinceCode.P_01)

    # Iterate over all
    for p in Province.iter_all():
        print(p.name)


To know if the data is up-to-date, check the ``__data_version__`` attribute of the module:

.. code-block:: python

    >>> import vietnam_provinces
    >>> vietnam_provinces.__data_version__
    '2026-02-21'


Install
-------

.. code-block:: sh

    python -m pip install vietnam-provinces
    # or
    uv add vietnam-provinces


This library is compatible with Python 3.12+.


Development
-----------

In development, this project has a tool to scrape and convert data from the National Statistics Office website.

The tool is tested on Linux only (may not run on Windows).

Update data
~~~~~~~~~~~

To scrape data directly from the National Statistics Office website and generate JSON:

.. code-block:: sh

    python3 -m dev scrape -f nested-json -o vietnam_provinces/data/nested-divisions.json

Or to generate Python code directly:

.. code-block:: sh

    python3 -m dev scrape -f python

You can run

.. code-block:: sh

    python3 -m dev scrape --help

to see more options of that tool.

Note that this tool is only available in the source folder (cloned from Git). It is not included in the distributable Python package.


Generate Python code
~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh

    python3 -m dev scrape -f python


Generate code for pre-2025 data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To generate Python code for pre-2025 administrative divisions (3-level hierarchy: Province -> District -> Ward):

.. code-block:: sh

    python3 -m dev gen-legacy -c dev/seed-data/Pre-2025-07/Xa_2025-01-04.csv

This generates two files:

1. *vietnam_provinces/legacy/codes.py* - Enum definitions for ``ProvinceCode``, ``DistrictCode``, ``WardCode``.
2. *vietnam_provinces/legacy/lookup.py* - Lookup mappings for ``Province``, ``District``, ``Ward`` objects.


Data source
~~~~~~~~~~~

- Name and code of provinces, and wards:  `National Statistics Office of Viet Nam <nso_vn_>`_.
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
.. _nso_vn: https://danhmuchanhchinh.nso.gov.vn/
.. _draft_new_units: https://chinhphu.vn/du-thao-vbqppl/du-thao-quyet-dinh-cua-thu-tuong-chinh-phu-ban-hanh-bang-danh-muc-va-ma-so-cac-don-vi-hanh-chinh-7546
.. _tb_ic: https://sotttt.thaibinh.gov.vn/tin-tuc/buu-chinh-vien-thong/tra-cuu-ma-vung-dien-thoai-co-dinh-mat-dat-ma-mang-dien-thoa2.html
.. _dataclass: https://docs.python.org/3/library/dataclasses.html
.. _pydantic: https://pypi.org/project/pydantic/
.. _quan: https://quan.hoabinh.vn
