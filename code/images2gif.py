import imageio.v2 as imageio
# from datetime import datetime
import sys
images = []

n = int(sys.argv[1])
moment = str(sys.argv[2])

m = len(str(n))
filenames = [f"frame_{i:0{m}d}.png" for i in range(1, n+1)]

for filename in filenames:
    images.append(imageio.imread(filename))


# now = datetime.now()
# moment = now.strftime("%m-%d_%H%M")
imageio.mimsave(f"pymovie_{moment}.gif", images)

