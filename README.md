# ๐ฅ video2gif
GIF ๋ณํ ์ฌ์ดํธ ๊ฐ๊ธฐ ๊ท์ฐฎ์์ ๋ง๋ค์๋๋ฐ ํ์ํ์  ๋ถ ์ฐ์ธ์ฅ


> There are 2 options to use this.  
> You can not only **download the GUI software** but **enter the command** into the terminal.  
> (ํ์ฐฎ์ง๋ง GUI ๋ง๋ค์๊ทธ๋ ์... ๊ทธ๋์ ์คํํ์ผ ๋ค์ด๋ก๋ ๋ฐ์์ ์ฌ์ฉํ์๊ฑฐ๋ ๊ทธ๋ฅ ๊น ํด๋ก  ํด์ ์ปค๋งจ๋ ์๋ ฅํด์ ์ฌ์ฉํ์๋ ๋ผ์ฉ.. ๋๊ฐ์ง ๋ฐฉ๋ฒ ์๋ ค๋๋ฆด๊ฒ์ฉ)

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

### GUI Software
1. Click 'Open File'.
2. Choose the video to convert
3. The converted gif file is located in the same directory.
![Sep-14-2022 20-51-44](https://user-images.githubusercontent.com/71140885/190146562-b72e6e35-7eca-4e16-b5d1-1360daac810b.gif)


### Command
```
python mp42gif.py --input [input source route] 
# Ex) python mp42gif --input '/Users/mindyeoi/Desktop/myVideo.mp4'
```

> ## To be continued...
> 1. GIF ์ฉ๋ ์ค์ด๊ธฐ - ์ฒดํฌ๋ฐ์ค๋ก
> 2. ์ฌ๋ฌ๊ฐ ํ์ผ ์ ํ