================
VietnamProvinces
================

.. image:: https://madewithlove.now.sh/vn?heart=true&colorA=%23ffcd00&colorB=%23da251d
.. image:: https://badgen.net/pypi/v/vietnam-provinces
   :target: https://pypi.org/project/vietnam-provinces/

[`English <english_>`_]

Thư viện cung cấp danh sách đơn vị hành chính Việt Nam (tỉnh thành, quận huyện, phường xã) với tên và mã số lấy theo `Tổng cục Thống kê <gso_vn_>`_.

Ví dụ:

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

Do lượng dữ liệu hơi lớn (10609 phường xã khắp Việt Nam) nên việc nạp và tách từ JSON sẽ chậm.


2. Kiểu dữ liệu Python

Dạng này có ích cho những ứng dụng nào cần truy cập dữ liệu thường xuyên (cắt bớt thời gian đọc file JSON và phân tách dữ liệu từ cấu trúc JSON). Chúng được định nghĩa bằng kiểu ``Enum`` để bạn có thể import vào code Python:

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


Nạp danh sách phường xã bằng cách này nhanh hơn từ JSON nhiều. Việc ở kiểu ``Enum`` cũng giúp người dùng thư viện tận dụng được tính năng gợi ý của phần mềm soạn thảo / IDE trong khi viết code, ngăn ngừa lỗi đánh máy.

Enum Ward có hai biến thể:

- ``WardEnum``: Có tên thành viên ở dạng mã số  (``W_28912``). Cách định nghĩa này có lợi cho việc tra tìm phường bằng mã số (đây là nhu cầu hay gặp nhất).

- ``WardDEnum``: Có tên thành viên ở dạng dễ đọc hơn (``D`` nghĩa là "descriptive"), giúp dễ hiểu hơn khi nhìn vào code ứng dụng. Ví dụ, khi nhìn vào ``WardDEnum.BT_PHAN_RI_CUA_22972``, lập trình viên sẽ đoán ngay được đây là "Phan Rí Cửa", thuộc tỉnh "Bình Thuận".

Tương tự, các cấp hành chính khác (District, Province) cũng có hai biến thể Enum.

Ví dụ tra cứu xã, huyện, tỉnh bằng mã số:

.. code-block:: python

    # Assume that you are loading user info from your database
    user_info = load_user_info()

    province_code = user_info['province_code']
    province = ProvinceEnum[f'P_{province_code}'].value

Không như ``ProvinceDEnum`` hay ``DistrictDEnum``, ``WardDEnum`` có mã phường xã trong tên thành viên của enum. Điều này là vì có quá nhiều xã trùng tên. Không có cách nào để đặt một định danh duy nhất cho phường xã chỉ với các chữ cái Latin không dấu, ngay cả khi có lồng thông tin quận huyện vào. Lấy ví dụ "Xã Đông Thành" và "Xã Đông Thạnh". Cả hai đều thuộc "Huyện Bình Minh" của "Vĩnh Long", nếu đặt định danh thì cả hai đều ra "DONG_THANH". Mặc dù Python cho phép dùng kí tự Unicode trong tên định danh, như "ĐÔNG_THẠNH", nhưng nó chưa thể áp dụng vào thực tiễn vì nhiều công cụ làm đẹp code (như `Black`_) vẫn tự loại bỏ các dấu đi.

Vì ``WardEnum`` có quá nhiều bản ghi (10609 tại thời điểm Tháng 2 2021) và không cần lắm với một số ứng dụng, tôi chuyển nó qua một module riêng, để không bị tự động nạp vào ứng dụng.

Kiểu dữ liệu của thành viên enum, như ``Province``, ``District`` and ``Ward``, có thể import từ cấp đầu của thư viện ``vietnam_provinces``.

.. code-block:: python

    >>> from vietnam_provinces import Province, District, Ward


Install
-------

.. code-block:: sh

    pip3 install vietnam-provinces


Thư viện này tương thích với Python 3.7 trở lên (do có sử dụng *dataclass*).


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

    python3 -m dev -i dev/seed-data/Xa_2021-02-03.csv -o vietnam_provinces/data/nested-divisions.json

Bạn có thể dùng lệnh

.. code-block:: sh

    python3 -m dev --help

để xem các tùy chọn mà công cụ có.

Lưu ý, công cụ này chỉ có mặt trong thư mục mã nguồn (lấy về từ Git). Nó không được kèm theo trong gói Python được xuất bản lên kho.


Sinh mã Python
~~~~~~~~~~~~~~

.. code-block:: sh

    python3 -m dev -i dev/seed-data/Xa_2021-02-03.csv -f python


Nguồn dữ liệu
~~~~~~~~~~~~~

- Tên và mã tỉnh thành, quận huyện, phường xã:  `Tổng cục Thống kê Việt Nam <gso_vn_>`_
- Mã vùng điện thoại: `Sở Thông tin và Truyền thông Thái Bình <tb_ic_>`_


Công trạng
----------

Mang đến cho bạn bởi `Nguyễn Hồng Quân <quan_>`_, sau hàng đêm và cuối tuần làm lụng.


.. _english: README.rst
.. _gso_vn: https://www.gso.gov.vn/
.. _tb_ic: https://sotttt.thaibinh.gov.vn/tin-tuc/buu-chinh-vien-thong/tra-cuu-ma-vung-dien-thoai-co-dinh-mat-dat-ma-mang-dien-thoa2.html
.. _dataclass: https://docs.python.org/3/library/dataclasses.html
.. _fast-enum: https://pypi.org/project/fast-enum/
.. _pydantic: https://pypi.org/project/pydantic/
.. _Black: https://github.com/psf/black
.. _quan: https://quan.hoabinh.vn
