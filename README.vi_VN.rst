================
VietnamProvinces
================

|image love| |image pypi|

[`English <english_>`_]

Thư viện cung cấp danh sách đơn vị hành chính Việt Nam (tỉnh thành, phường xã, không còn cấp quận huyện từ Tháng 7, 2025) với tên và mã số lấy theo `Cục Thống kê - Bộ Tài chính <nso_vn_>`_.

Ví dụ:

.. code-block:: json

  {
    "name": "Tỉnh Tuyên Quang",
    "code": 8,
    "codename": "tuyen_quang",
    "division_type": "tỉnh",
    "phone_code": 207,
    "wards": [
      {
        "name": "Xã Nấm Dẩn",
        "code": 1141,
        "codename": "xa_nam_dan",
        "division_type": "xã",
        "short_codename": "nam_dan"
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

Thư viện này cung cấp dữ liệu dưới các dạng sau:

1. JSON

Dạng này phù hợp cho những ứng dụng nào không cần truy cập thường xuyên, khi mà việc nạp chuỗi JSON lên và tách thông tin từ nó không thành vấn đề. Các file JSON được giữ trong thư mục *data*. Bạn có thể lấy đường dẫn file từ biến ``vietnam_provinces.NESTED_DIVISIONS_JSON_PATH``.

Lưu ý rằng biến này chỉ cung cấp đường dẫn file, không phải nội dung file. Ứng dụng có thể dùng bất cứ phương pháp nào tùy ý để phân tích JSON. Ví dụ:

.. code-block:: python

    import orjson
    import rapidjson
    from vietnam_provinces import NESTED_DIVISIONS_JSON_PATH

    # Với rapidjson
    with NESTED_DIVISIONS_JSON_PATH.open() as f:
        rapidjson.load(f)

    # Với orjson
    orjson.loads(NESTED_DIVISIONS_JSON_PATH.read_bytes())


2. Kiểu dữ liệu Python

Dạng này có ích cho những ứng dụng nào cần truy cập dữ liệu thường xuyên (cắt bớt thời gian đọc file JSON và phân tách dữ liệu từ cấu trúc JSON).
Có hai loại đối tượng: `Province` / `Ward` đại diện cho một tỉnh, xã và `ProvinceCode` / `WardCode` là mã số của tỉnh, xã ở dạng `enum`.
Bạn có thể import vào code Python để dùng ngay.

.. code-block:: python

    >>> from vietnam_provinces import ProvinceCode, Province, WardCode, Ward

    >>> Province.from_code(ProvinceCode.P_15)
    Province(name='Tỉnh Lào Cai', code=<ProvinceCode.P_15: 15>, division_type=<VietNamDivisionType.TINH: 'tỉnh'>, codename='lao_cai', phone_code=214)

    >>> Ward.from_code(23425)
    Ward(name='Xã Tu Mơ Rông', code=<WardCode.W_23425: 23425>, division_type=<VietNamDivisionType.XA: 'xã'>, codename='xa_tu_mo_rong', province_code=<ProvinceCode.P_51: 51>)

    >>> # Tìm kiếm phường xã hiện tại bằng dữ liệu cũ (trước 2025)
    >>> Ward.search_from_legacy(name='phu my')
    (Ward(name='Phường Phú Mỹ', ...), Ward(name='Xã Phú Mỹ', ...), ...)

    >>> # Lấy các phường xã cũ đã được sáp nhập để tạo thành phường xã mới
    >>> ward = Ward.from_code(4)  # Phường Ba Đình
    >>> ward.get_legacy_sources()
    (Ward(name='Phường Trúc Bạch', ...), Ward(name='Phường Quán Thánh', ...), ...)

Các kiểu dữ liệu trước 2025 có thể được sử dụng như sau:

.. code-block:: python

    from vietnam_provinces.legacy import Province, District, Ward
    from vietnam_provinces.legacy.codes import ProvinceCode

    # Tra cứu theo mã
    province = Province.from_code(ProvinceCode.P_01)

    # Duyệt qua tất cả
    for p in Province.iter_all():
        print(p.name)


Để biết dữ liệu đã được cập nhật chưa, kiểm tra thuộc tính ``__data_version__`` của module:

.. code-block:: python

    >>> import vietnam_provinces
    >>> vietnam_provinces.__data_version__
    '2026-02-21'


Cài đặt
-------

.. code-block:: sh

    pip3 install vietnam-provinces


Thư viện này tương thích với Python 3.12 trở lên.


Phát triển
-----------

Trong lúc được phát triển, dự án này có một công cụ để cào và chuyển đổi dữ liệu từ website Cục Thống kê.

Công cụ này chỉ chạy được trên Linux (có thể không chạy trên Windows).

Cập nhật dữ liệu
~~~~~~~~~~~~~~~~

Để cào dữ liệu trực tiếp từ website Cục Thống kê và tạo file JSON:

.. code-block:: sh

    python3 -m dev scrape -f nested-json -o vietnam_provinces/data/nested-divisions.json

Hoặc để sinh mã Python trực tiếp:

.. code-block:: sh

    python3 -m dev scrape -f python

Bạn có thể dùng lệnh

.. code-block:: sh

    python3 -m dev scrape --help

để xem các tùy chọn mà công cụ có.

Lưu ý, công cụ này chỉ có mặt trong thư mục mã nguồn (lấy về từ Git). Nó không được kèm theo trong gói Python được xuất bản lên kho.


Sinh mã Python
~~~~~~~~~~~~~~

.. code-block:: sh

    python3 -m dev scrape -f python


Sinh mã cho dữ liệu trước 2025
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Để sinh mã Python cho đơn vị hành chính trước 2025 (phân cấp 3 cấp: Tỉnh -> Huyện -> Xã):

.. code-block:: sh

    python3 -m dev gen-legacy -c dev/seed-data/Pre-2025-07/Xa_2025-01-04.csv

Lệnh này tạo ra hai file:

1. *vietnam_provinces/legacy/codes.py* - Định nghĩa enum cho ``ProvinceCode``, ``DistrictCode``, ``WardCode``.
2. *vietnam_provinces/legacy/lookup.py* - Bảng tra cứu cho các đối tượng ``Province``, ``District``, ``Ward``.


Nguồn dữ liệu
~~~~~~~~~~~~~

- Tên và mã tỉnh thành, phường xã:  `Cục Thống kê - Bộ Tài chính <nso_vn_>`_.
- Mã vùng điện thoại: `Sở Thông tin và Truyền thông Thái Bình <tb_ic_>`_.


Công trạng
----------

Mang đến cho bạn bởi `Nguyễn Hồng Quân <quan_>`_, sau hàng đêm và cuối tuần làm lụng.


.. |image love| image:: https://madewithlove.now.sh/vn?heart=true&colorA=%23ffcd00&colorB=%23da251d
.. |image pypi| image:: https://badgen.net/pypi/v/vietnam-provinces
   :target: https://pypi.org/project/vietnam-provinces/

.. _english: README.rst
.. _nso_vn: https://danhmuchanhchinh.nso.gov.vn/
.. _draft_new_units: https://chinhphu.vn/du-thao-vbqppl/du-thao-quyet-dinh-cua-thu-tuong-chinh-phu-ban-hanh-bang-danh-muc-va-ma-so-cac-don-vi-hanh-chinh-7546
.. _tb_ic: https://sotttt.thaibinh.gov.vn/tin-tuc/buu-chinh-vien-thong/tra-cuu-ma-vung-dien-thoai-co-dinh-mat-dat-ma-mang-dien-thoa2.html
.. _dataclass: https://docs.python.org/3/library/dataclasses.html
.. _pydantic: https://pypi.org/project/pydantic/
.. _quan: https://quan.hoabinh.vn
