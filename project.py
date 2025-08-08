import streamlit as st

with st.sidebar:
	image = 'duongdomic.jpg'
	st.image(image, caption='Dương Domic')
	st.write('Họ và tên: Trần Đăng Dương')
	st.write('Nghệ danh: Dương Domic')
	st.write('Dương Domic (Trần Đăng Dương), sinh 31/8/2000 tại Hải Dương, là ca sĩ, rapper, sáng tác nhạc người Việt. Nổi bật từ Anh Trai Say Hi 2024 với các ca khúc như Tràn Bộ Nhớ, Mất Kết Nối, anh thuộc DAO Entertainment, từng là thực tập sinh IF Entertainment. Sở hữu chiều cao 1m85, phong cách Hiphop, R&B, Pop, anh giành giải "Gương mặt mới xuất sắc" Làn Sóng Xanh 2023 và là thành viên nhóm Mopius.')
st.title('Bài hát yêu thích')
st.write('Mất kết nối')
audio = open('Mất kết nối(Dương Domic).mp3')
st.audio(audio, format='audio/mp4')	
st.title('MV yêu thích')
st.write('Hào quang')
video = 'https://www.youtube.com/watch?v=Tr5Ty9ZngvE'
st.video(video, format='video/mp4')