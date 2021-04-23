from pymagnitude import Magnitude, MagnitudeUtils

vectors = Magnitude("https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/chive-1.1-mc90-aunit.magnitude", stream=True)
# vectors.query("春")
print(vectors.similarity("私","僕"))