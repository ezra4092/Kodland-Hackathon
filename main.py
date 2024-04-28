import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello!! bot is ready, I am a {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    # kode untuk bot menerima gambar
    if ctx.message.attachments: 
        for file in ctx.message.attachments: 
            file_name = file.filename 
            file_url = file.url
            await file.save(f'./{file.filename}')
            hasil = get_class(model_path='keras_model.h5', labels_path='labels.txt', image_path=f'./{file.filename}')
            
            # kode untuk memproses gambar (ubah dengan melihat labels.txt)
            if hasil[0] == 'Polusi Air\n' and hasil[1] >= 0.65:
                await ctx.send('Gambar tersebut adalah polusi Air. Polusi air merupakan bercampurnya zat pencemar dan air, melalui sungai, pantai, danau, dan air tanah, yang mengakibatkan kualitas air menurun.\n')
                await ctx.send('Dampak dari polusi air adalah jika kita mengonsumsi air yang tercemar dapat menyebabkan berbagai penyakit seperti diare, kolera, keracunan, dan bahkan kematian. Selain itu Polusi air dapat merusak habitat air, membunuh hewan dan tumbuhan, dan mengganggu rantai makanan.')
                await ctx.send('Berikut beberapa langkah yang bisa dilakukan untuk mencegah polusi air:')
                await ctx.send('1. Jangan membuang sampah sembarangan, terutama ke aliran air. Pisahkan sampah organik dan non-organik, dan buanglah pada tempatnya.')
                await ctx.send('2. Hindari penggunaan pupuk dan pestisida kimia di kebun atau area pertanian, karena dapat mencemari air tanah.')
                await ctx.send('3. Daur ulang sampah plastik, kertas, dan logam untuk mengurangi jumlah sampah yang dibuang ke tempat pembuangan akhir.')
            elif hasil[0] == 'Polusi Udara\n' and hasil[1] >= 0.65:
                await ctx.send('Gambar tersebut adalah polusi Udara. Polusi udara adalah pencemaran yang tercipta di udara karena masuknya bahan pencemar seperti sulfur oksida (SOx), karbon monoksida (CO), karbon dioksida (CO2), nitrogen oksida (NOx) dan hidrokarbon di atas batas normal.\n')
                await ctx.send('Dampak dari polusi udara adalah Polusi udara dapat menyebabkan berbagai penyakit pernapasan seperti asma, bronkitis, dan pneumonia. Selain itu Polusi udara dapat menyebabkan hujan asam, kabut asap, dan perubahan iklim.')
                await ctx.send('Berikut beberapa langkah yang bisa dilakukan untuk mencegah polusi udara:')
                await ctx.send('1. Gunakan transportasi umum, bersepeda, atau berjalan kaki untuk mengurangi emisi gas buang kendaraan.')
                await ctx.send('2. Hindari membakar sampah karena dapat menghasilkan asap yang mengandung polutan berbahaya.')
                await ctx.send('3. Menanam pohon karena dapat membantu menyerap polutan dari udara.')
            elif hasil[0] == 'Polusi Cahaya\n' and hasil[1] >= 0.65:
                await ctx.send('Gambar tersebut adalah polusi udara. Polusi cahaya adalah suatu peristiwa yang disebabkan oleh cahaya yang berlebihan yang memengaruhi kesehatan dan kenyamanan makhluk hidup di ekosistem.\n')
                await ctx.send('Dampak polusi cahaya adalah jika paparan cahaya berlebihan pada malam hari dapat mengganggu pola tidur, memicu stres, dan meningkatkan risiko depresi.')
                await ctx.send('Berikut beberapa langkah yang bisa dilakukan untuk mencegah polusi cahaya:')
                await ctx.send('1. Hindari penggunaan lampu dekoratif atau pencahayaan berlebihan di luar ruangan.')
                await ctx.send('2. Hindari penggunaan lampu dengan warna biru atau putih terang, karena warna-warna ini lebih berkontribusi pada polusi cahaya.')
                await ctx.send('3. Hindari penggunaan lampu sorot yang tidak perlu, seperti untuk menerangi pepohonan atau bangunan.')
            elif hasil[0] == 'Polusi Suara\n' and hasil[1] >= 0.65:
                await ctx.send('Gambar tersebut adalah polusi suara. Polusi suara adalah kebisingan yang mengganggu indra pendengaran.\n')
                await ctx.send('Dampak polusi suara jika paparan suara keras dalam jangka panjang dapat menyebabkan kerusakan pada sel-sel rambut di telinga bagian dalam, yang berakibat pada hilangnya pendengaran permanen (tuli).')
                await ctx.send('Berikut beberapa langkah yang bisa dilakukan untuk mencegah polusi suara:')
                await ctx.send('1. Hindari mendengarkan musik atau menonton TV dengan volume yang tinggi, terutama di malam hari.')
                await ctx.send('2. Jika sedang berkendara, gunakan klakson hanya pada saat benar-benar diperlukan.')
                await ctx.send('3. Pastikan kendaraan Anda dalam kondisi prima untuk meminimalkan kebisingan mesin.')
            elif hasil[0] == 'Polusi Tanah\n' and hasil[1] >= 0.65:
                await ctx.send('Gambar tersebut adalah polusi tanah. Polusi tanah adalah masuknya bahan pencemar secara langsung atau tidak langsung ke dalam tanah. Jika polutan ini masuk ke tanah secara langsung, tanah yang terkontaminasi melepaskan zat beracun ke udara.\n')
                await ctx.send('Dampak polusi tanah adalah dapat mengurangi kesuburan tanah, sehingga menurunkan hasil panen dan mengganggu ketahanan pangan. Selain itu jika mengonsumsi tanaman yang ditanam di tanah tercemar dapat menyebabkan berbagai penyakit, seperti kanker dan keracunan logam.')
                await ctx.send('Berikut beberapa langkah yang bisa dilakukan untuk mencegah polusi tanah:')
                await ctx.send('1. Hindari penggunaan plastik sekali pakai dan gunakan alternatif yang lebih ramah lingkungan, seperti tas kain atau botol minum isi ulang.')
                await ctx.send('2. Jangan membuang sampah sembarangan, terutama ke tanah. Pisahkan sampah organik dan non-organik, dan buanglah pada tempatnya.')
                await ctx.send('3. Hindari penggunaan pupuk dan pestisida kimia di kebun atau area pertanian, karena dapat mencemari tanah.')
            elif hasil[0] == 'Polusi Visual\n' and hasil[1] >= 0.65:
                await ctx.send('Gambar tersebut adalah polusi visual. Polusi visual terjadi ketika tata ruang suatu area tidak terorganisir dengan baik, seperti keberadaan monumen yang tidak esensial, berlebihnya papan iklan, kabel listrik yang berantakan, dan sampah menumpuk di pinggir jalan.\n')
                await ctx.send('Dampak polusi visualmisalnya papan reklame yang berlebihan, dapat mengganggu konsentrasi pengemudi dan meningkatkan risiko kecelakaan.')
                await ctx.send('Berikut beberapa langkah yang bisa dilakukan untuk mencegah polusi visual:')
                await ctx.send('1. Hindari memasang iklan atau spanduk yang berlebihan di rumah atau tempat usaha.')
                await ctx.send('2. Tidak mencoret-coret tembok atau fasilitas umum.')
                await ctx.send('3. Pemerintah membuat peraturan dan undang-undang yang mengatur tentang pemasangan iklan, spanduk, dan papan reklame.')
            else:
                await ctx.send('Tidak dapat mengenali gambar mu. Kemungkinan salah format/clur/corrupt.')
                await ctx.send('KIRIM GAMBAR BARU!!!')
    else:
        await ctx.send('Gambar tidak valid / Tidak ada.')
        await ctx.send('KIRIM GAMBAR BARU!!!')


bot.run("Masukan token bot disini!")