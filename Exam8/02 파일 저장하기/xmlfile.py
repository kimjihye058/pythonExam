import xml.etree.ElementTree as ET      # xml.etree.ElementTree 모듈을 ET라고 이름 짓기
from xml.etree.ElementTree import Element, SubElement       # 필요한 클래스(Element)와 함수(SubElement) 불러오기
# Element: 전달된 문자여러을 태그(요소)의 이름으로 하는 태그 객체를 생성한다.
# SubElement: 첫 번째 파라미터로 전달된 태그(요소)를 부모로 하고 전달된 문자열을 태그의 이름으로 하는 자식 태그 객체를 생성한다.

root = Element("movie")
title = SubElement(root, "title")
title.text = "트렌스포머"
genre = SubElement(root, "genre")
genre.text = "SF"
rating = SubElement(root, "rating")
rating.text = "8"

ET.ElementTree(root).write("movie.xml", encoding="UTF-8", xml_declaration = True)       # .xml파일 생성