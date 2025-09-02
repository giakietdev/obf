
`obf.py` là một công cụ obfuscation (làm rối) mã Python mạnh mẽ và phức tạp, được phát triển bởi Trương Quang Thắng. Công cụ này sử dụng nhiều kỹ thuật obfuscation tiên tiến để bảo vệ mã nguồn Python khỏi việc reverse engineering và phân tích.

## Thông tin tác giả
- **Tác giả**: Trương Quang Thắng
- **Địa chỉ**: Thái Bình, Việt Nam
- **Phiên bản**: 1.1.7
- **Liên hệ**: https://www.facebook.com/quangthang.8507
- **Discord**: thick1minh

### 1. Import và Dependencies
```python
import ast
import ast, random, math
from giakiethoang import Add, Center, Anime, Colors, Colorate, Write, System, Col
from getpass import getpass
__import__('sys').setrecursionlimit(999999999)
```

### 2. Các lớp chính

#### 2.1 AntiDebugUtils
**Mục đích**: Tạo các kiểm tra chống debug để phát hiện và ngăn chặn việc debug mã.

**Các tính năng chính**:
- Kiểm tra các module debug phổ biến: `pdb`, `bdb`, `pydevd`, `debugpy`, `ptvsd`
- Kiểm tra biến môi trường debug: `PYTHONINSPECT`, `PYTHONDEBUG`, `PYDEVD_DISABLE_FILE_VALIDATION`
- Kiểm tra các tiến trình debug: `gdb`, `lldb`, `windbg`, `ollydbg`, `x64dbg`, `ida64`
- Kiểm tra timing để phát hiện debugger
- Kiểm tra breakpoint và trace
- Kiểm tra parent process để phát hiện debugger

#### 2.2 AntiVMUtils
**Mục đích**: Tạo các kiểm tra chống Virtual Machine để phát hiện môi trường ảo hóa.

**Các tính năng chính**:
- Kiểm tra các tiến trình VM: `vmsrvc.exe`, `vmusrvc.exe`, `vmtoolsd.exe`, `vboxservice.exe`
- Kiểm tra registry Windows để phát hiện VM
- Kiểm tra các file VM phổ biến
- Kiểm tra MAC address prefixes của VM
- Kiểm tra hardware và BIOS để phát hiện VM

#### 2.3 RuntimeKeyUtils
**Mục đích**: Tạo và xác thực runtime key dựa trên thông tin hệ thống.

**Các tính năng chính**:
- Tạo key dựa trên: `platform.node()`, `platform.processor()`, `platform.machine()`, `platform.system()`
- Xác thực key với multiple checks
- Time-based validation
- Hash-based validation sử dụng MD5 và SHA256

#### 2.4 EnhancedControlFlowUtils
**Mục đích**: Tạo các kỹ thuật obfuscation control flow nâng cao.

**Các tính năng chính**:
- Tạo junk functions để làm rối code
- Anti-timing checks
- Control flow obfuscation với state machine
- Chuyển đổi cấu trúc điều khiển thành dạng phức tạp

#### 2.5 AdvancedEncryptionUtils
**Mục đích**: Cung cấp các thuật toán mã hóa nâng cao.

**Các thuật toán hỗ trợ**:
- **AES Encryption**: Mã hóa XOR đơn giản
- **ChaCha20 Encryption**: Mã hóa stream cipher
- **RC4 Encryption**: Thuật toán RC4 hoàn chỉnh
- **XOR Encryption**: Mã hóa XOR cơ bản
- **Base91 Encoding**: Encoding base91 tùy chỉnh
- **LZMA Compression**: Nén dữ liệu với LZMA

#### 2.6 FakeCodeGenerator
**Mục đích**: Tạo code giả để làm rối và che giấu logic thực.

**Các tính năng chính**:
- Tạo fake functions với các phép toán ngẫu nhiên
- Tạo useless loops để làm chậm phân tích
- Tạo các biến và hàm không liên quan

#### 2.7 StateMachineFlattener
**Mục đích**: Chuyển đổi functions thành state machine để làm rối control flow.

**Các tính năng chính**:
- Flatten function body thành state machine
- Sử dụng while loops với state variables
- Tạo cấu trúc điều khiển phức tạp

#### 2.8 DynamicImportRenamer
**Mục đích**: Tạo dynamic imports để che giấu việc import modules.

**Các tính năng chính**:
- Tạo dynamic imports cho các module phổ biến
- Sử dụng character-by-character construction
- Che giấu tên module

#### 2.9 ControlFlowTransformer
**Mục đích**: Chuyển đổi cấu trúc điều khiển thành dạng phức tạp.

**Các tính năng chính**:
- Transform if-else thành complex state
- Transform loops thành complex state
- Sử dụng iterator pattern

### 3. Các Transformer chính

#### 3.1 AdvancedObfuscationTransformer
**Mục đích**: Áp dụng các kỹ thuật obfuscation nâng cao.

**Quy trình**:
1. Thêm encryption layers
2. Thêm fake code
3. Thêm useless loops
4. Flatten functions
5. Thêm dynamic imports
6. Transform control flow

#### 3.2 SecurityTransformer
**Mục đích**: Áp dụng các biện pháp bảo mật.

**Quy trình**:
1. Thêm anti-debug checks
2. Thêm anti-VM checks
3. Thêm runtime key validation
4. Thêm anti-timing checks
5. Enhance control flow

#### 3.3 BiOpaqueTransformer
**Mục đích**: Tạo opaque predicates để làm rối logic.

**Các tính năng chính**:
- Tạo bogus body cho các statements
- Generate roadline cho boolean values
- Tạo opaque predicates với random operations
- Fix function calls với additional parameters

#### 3.4 ExceptionJumpTransformer
**Mục đích**: Sử dụng exception handling để làm rối control flow.

**Các tính năng chính**:
- Tạo custom exception class `Obfuscation`
- Sử dụng try-except để jump giữa các blocks
- Tạo junk exception handlers
- Shuffle exception handlers

#### 3.5 CallTransformer
**Mục đích**: Obfuscate function calls.

**Các tính năng chính**:
- Transform builtin function calls
- Sử dụng `getattr` để gọi functions
- Tạo dynamic function resolution

### 4. String Obfuscation (OBF_STRING)

#### 4.1 Các tính năng chính
- **Token-based obfuscation**: Phân tích và obfuscate từng token
- **Builtin obfuscation**: Che giấu việc sử dụng builtin functions
- **String protection**: Bảo vệ strings với các kỹ thuật encoding
- **Import obfuscation**: Che giấu imports
- **Marshal compilation**: Compile code thành bytecode

#### 4.2 Các phương thức obfuscation
- **Boolean obfuscation**: `_obf_bool()`
- **Integer obfuscation**: `_obf_int()`, `_adv_int()`
- **String obfuscation**: `_obf_str()`, `_adv_str()`
- **Byte obfuscation**: `OBF_BYTE()`

### 5. Utility Classes

#### 5.1 Utils
**Các phương thức tiện ích**:
- `randomize_name()`: Tạo tên biến ngẫu nhiên
- `generate_next_num()`: Tạo số tiếp theo
- `find_parent()`: Tìm parent node
- `find_class()`: Tìm class definition
- `get_chance()`: Tạo random chance

#### 5.2 MutatorUtils
**Mục đích**: Mutation-based obfuscation.

**Các tính năng chính**:
- Generate stack elements cho integers
- Proceed integer assignments với ladder obfuscation
- Proceed list assignments
- Generate binary operations cho integers và floats
- Proceed constants với complex expressions

### 6. ObfuscatorSettings
**Mục đích**: Quản lý cấu hình các transformer.

**Các phương thức**:
- `exceptionjmp_transformer()`: Thêm exception jump transformer
- `call_transformer()`: Thêm call transformer
- `biopaque_transformer()`: Thêm biopaque transformer
- `security_transformer()`: Thêm security transformer
- `advanced_obfuscation_transformer()`: Thêm advanced obfuscation transformer

### 7. Main Functions

#### 7.1 OBF_Import()
**Mục đích**: Obfuscate import statements.

#### 7.2 OBF_Spam()
**Mục đích**: Áp dụng tất cả các transformer với cấu hình mặc định.

#### 7.3 compl()
**Mục đích**: Compile code thành bytecode với marshal, zlib, và base64.

#### 7.4 check_syntax()
**Mục đích**: Kiểm tra syntax của code sau khi obfuscate.

### 8. User Interface

#### 8.1 Banner và Styling
- Sử dụng thư viện `giakiethoang` để tạo banner đẹp
- Color scheme với cyan và purple
- Dynamic color mixing

#### 8.2 Main Function
**Quy trình chính**:
1. Hiển thị banner
2. Nhập file input
3. Đọc và kiểm tra file
4. Nhập cấu hình obfuscation:
   - String obfuscation version (v1/v2)
   - Exception jump protection (yes/no)
   - Wall compile (yes/no)
5. Áp dụng obfuscation
6. Kiểm tra syntax
7. Lưu file output

### 9. Các kỹ thuật obfuscation được sử dụng

#### 9.1 Control Flow Obfuscation
- State machine flattening
- Exception-based control flow
- Opaque predicates
- Junk code injection

#### 9.2 Data Obfuscation
- String encoding/encryption
- Integer obfuscation với arithmetic operations
- Variable name randomization
- Constant folding

#### 9.3 Anti-Analysis
- Anti-debugging techniques
- Anti-VM detection
- Runtime key validation
- Timing-based checks

#### 9.4 Code Structure Obfuscation
- Function cloning
- Dynamic imports
- Builtin function obfuscation
- Import statement obfuscation

### 10. Cách sử dụng

#### 10.1 Chạy chương trình
```bash
python obf.py
```

#### 10.2 Các tùy chọn
1. **File input**: Đường dẫn đến file Python cần obfuscate
2. **String obfuscation**: 
   - v1 (x): Phiên bản đơn giản
   - v2 (y): Phiên bản nâng cao (khuyến nghị)
3. **Exception jump protection**:
   - no (x): Không bảo vệ
   - yes (y): Có bảo vệ
4. **Wall compile**:
   - no (x): Không compile
   - yes (y): Compile thành bytecode

#### 10.3 Output
- File output sẽ được lưu với prefix "obf-"
- Ví dụ: `script.py` → `obf-script.py`

### 11. Hạn chế và lưu ý

#### 11.1 Hạn chế
- Không hỗ trợ `global` statements
- Có thể làm chậm execution
- File size có thể tăng đáng kể
- Một số IDE có thể không hiểu được code sau obfuscation

#### 11.2 Lưu ý bảo mật
- Obfuscation không phải là mã hóa, chỉ làm khó đọc
- Vẫn có thể bị reverse engineering bởi expert
- Nên kết hợp với các biện pháp bảo mật khác

### 12. Cấu trúc file output

#### 12.1 Khi không có Wall Compile
- Code Python đã được obfuscate
- Có thể đọc được nhưng rất khó hiểu
- Chứa nhiều junk code và fake functions

#### 12.2 Khi có Wall Compile
- C4
- Cầnode được compile thành bytecode
- Sử dụng marshal, zlib, base6 runtime để execute
- Khó reverse engineering hơn

### 13. Performance Impact

#### 13.1 Thời gian obfuscation
- Phụ thuộc vào kích thước file
- Thường mất vài giây đến vài phút

#### 13.2 Runtime performance
- Code sau obfuscation chạy chậm hơn
- Do có nhiều junk code và checks
- Impact có thể từ 10-50% tùy thuộc vào cấu hình

### 14. Troubleshooting

#### 14.1 Lỗi thường gặp
- **Syntax Error**: Code input có lỗi syntax
- **Global Error**: File chứa global statements
- **Import Error**: Thiếu dependencies

#### 14.2 Giải pháp
- Kiểm tra syntax file input
- Loại bỏ global statements
- Cài đặt đầy đủ dependencies

Công cụ này phù hợp cho:
- Bảo vệ intellectual property
- Che giấu business logic
- Tăng độ khó reverse engineering
- Bảo vệ API keys và sensitive data

**Lưu ý quan trọng**: Việc sử dụng obfuscation cần tuân thủ các quy định pháp luật và đạo đức. Không nên sử dụng để che giấu malware hoặc các hoạt động bất hợp pháp.
