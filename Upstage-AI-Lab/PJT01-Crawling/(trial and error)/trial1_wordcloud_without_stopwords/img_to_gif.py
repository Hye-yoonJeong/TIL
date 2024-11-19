import os
import imageio


import matplotlib.animation as animation

png_dir = '.\level03\wordcloud'
gif_path = '.\level03\wordcloud\wordcloud.gif'

png_files = [file for file in os.listdir(png_dir) if file.endswith('.png')]

png_files.sort()

images = []
for png_file in png_files :
    file_path = os.path.join(png_dir, png_file)
    images.append(imageio.imread(file_path))

imageio.mimsave(gif_path, images, duration=2, loop=0)

print(f'GIF saved at: {gif_path}')





# ani = animation.ArtistAnimation()
# fig = plt.figure(figsize=(8,8))
# plt.axis("off")
# ims = [[plt.imshow(np.transpose(i,(1,2,0)), animated=True)] for i in GAN_01_FeedForward_GAN]

# ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=1000, blit=True)
# HTML(ani.to_jshtml())

