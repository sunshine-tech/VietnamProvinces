================
VietnamProvinces
================

|image love| |image pypi|

[`English <english_>`_]

Thư viện cung cấp danh sách đơn vị hành chính Việt Nam (tỉnh thành, phường xã, không còn cấp quận huyện từ Tháng 7, 2025) với tên và mã số lấy theo `Dự thảo Quyết định của Thủ tướng Chính phủ ban hành Bảng danh mục và mã số các đơn vị hành chính Việt Nam <draft_new_units_>`_.

Ví dụ:

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
    Province(name='Lào Cai', code=15, division_type=<VietNamDivisionType.TINH: 'tỉnh'>, codename='lao_cai', phone_code=214)

    >>> Ward.from_code(WardCode.W_01234)
    Ward(name='Xã Yên Thành', code=1234, division_type=<VietNamDivisionType.XA: 'xã'>, codename='xa_yen_thanh', province_code=8)


Cài đặt
-------

.. code-block:: sh

    pip3 install vietnam-provinces


Thư viện này tương thích với Python 3.10 trở lên.


Phát triển
-----------

Trong lúc được phát triển, dự án này có một công cụ để chuyển đổi dữ liệu từ nguồn của Nhà nước.

Công cụ này không cào dữ liệu trực tiếp từ website của Chính phủ vì dữ liệu này hiếm khi thay đổi (không đáng để xây dựng một tính năng mà bạn sau mỗi chục năm mới cần phải dùng) và vì các website này cung cấp dữ liệu ở định dạng của Microsoft Office, không thân thiện lắm với máy.

Cập nhật dữ liệu
~~~~~~~~~~~~~~~~

Trong tương lai, nếu chính quyền sắp xếp lại các đơn vị hành chính, ta cần thu thập lại dữ liệu từ website GSOVN. Các bước như sau:

- Vào: https://danhmuchanhchinh.gso.gov.vn/ (đường link này có thể thay đổi khi `GSOVN <gso_vn_>`_ thay mới phần mềm của họ).
- Tìm nút "Xuất Excel".
- Tích chọn "Quận Huyện Phường Xã".
- Bấm nút và tải về file Excel (xls).
- Dùng LibreOffice để chuyển đổi file Excel sang dạng CSV. Ví dụ ta đặt tên file CSV là *Xa_2021-02-03.csv*.
- Chạy công cụ này để tách, sắp xếp dữ liệu ở dạng JSON:

.. code-block:: sh

    python3 -m dev -w dev/seed-data/2025-07/Cap-xa.csv -p dev/seed-data/2025-07/Cap-tinh.csv -f nested-json

Bạn có thể dùng lệnh

.. code-block:: sh

    python3 -m dev --help

để xem các tùy chọn mà công cụ có.

Lưu ý, công cụ này chỉ có mặt trong thư mục mã nguồn (lấy về từ Git). Nó không được kèm theo trong gói Python được xuất bản lên kho.


Sinh mã Python
~~~~~~~~~~~~~~

.. code-block:: sh

    python3 -m dev -w dev/seed-data/2025-07/Cap-xa.csv -p dev/seed-data/2025-07/Cap-tinh.csv -f python


Nguồn dữ liệu
~~~~~~~~~~~~~

- Tên và mã tỉnh thành, phường xã:  `Tổng cục Thống kê Việt Nam <gso_vn_>`_.
- Mã vùng điện thoại: `Sở Thông tin và Truyền thông Thái Bình <tb_ic_>`_.


Công trạng
----------

Mang đến cho bạn bởi `Nguyễn Hồng Quân <quan_>`_, sau hàng đêm và cuối tuần làm lụng.


.. |image love| image:: https://madewithlove.now.sh/vn?heart=true&colorA=%23ffcd00&colorB=%23da251d
.. |image pypi| image:: https://badgen.net/pypi/v/vietnam-provinces
   :target: https://pypi.org/project/vietnam-provinces/
.. _english: README.rst
.. _gso_vn: https://danhmuchanhchinh.gso.gov.vn/
.. _draft_new_units: https://chinhphu.vn/du-thao-vbqppl/du-thao-quyet-dinh-cua-thu-tuong-chinh-phu-ban-hanh-bang-danh-muc-va-ma-so-cac-don-vi-hanh-chinh-7546
.. _tb_ic: https://sotttt.thaibinh.gov.vn/tin-tuc/buu-chinh-vien-thong/tra-cuu-ma-vung-dien-thoai-co-dinh-mat-dat-ma-mang-dien-thoa2.html
.. _dataclass: https://docs.python.org/3/library/dataclasses.html
.. _pydantic: https://pypi.org/project/pydantic/
.. _quan: https://quan.hoabinh.vn
