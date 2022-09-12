# 🎥 video2gif
GIF 변환 사이트 가기 귀찮아서 만들었는데 필요하신 분 쓰세욥


> There are 2 options to use this.  
> You can not only **download the GUI software** but **enter the command** into the terminal.  
> (하찮지만 GUI 만들었그든요... 그래서 실행파일 다운로드 받아서 사용하시거나 그냥 깃 클론 해서 커맨드 입력해서 사용하셔도 돼용.. 두가지 방법 알려드릴게용)

## Installation

### GUI software (.exe file)
1. Download the software to click [here](https://drive.google.com/file/d/1eZHgNFQtStQqf6wx2HLXp4e7-6XvfHQF/view?usp=sharing).
2. Just Enjoy it!
   * But it may take a while to initialize.
   

### Command
1. Clone this repo.
   ```
   git clone https://github.com/MINDYEOI/video2gif.git
   ```

2. Move to the **video2gif** directory.

3. Install the requirements.
   ```
   pip install -r requirements.txt
   ```


## Usage
> ⚠️ You can use only **mp4 & avi to gif converter** now. <br>
> ⚠️ It may not work when the input source route has special character such as ♥, ♫, ★ and so on.

### GUI Software
1. Click 'Open File'.
2. Choose the video to convert
3. The converted gif file is located in the same directory.
![Sep-13-2022 01-19-01](https://user-images.githubusercontent.com/71140885/189705507-86ecb7ca-942a-4168-8820-d3175e18b1e5.gif)

### Command
```
python mp42gif.py --input [input source route] 
# Ex) python mp42gif --input '/Users/mindyeoi/Desktop/myVideo.mp4'
```