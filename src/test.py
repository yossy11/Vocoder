import pyworld as pw
import soundfile as sf


def main():
    # read
    x, fs = sf.read('Datas/vaiueo2d.wav')

    # extract features
    f0, sp, ap = pw.wav2world(x, fs)    # use default options

    # synthesize features
    y_default = pw.synthesize(f0, sp, ap, fs, pw.default_frame_period)

    # write
    sf.write('test/default.wav', y_default, fs)

    y_f0_x2 = pw.synthesize(f0*2, sp, ap, fs, pw.default_frame_period)
    sf.write('test/f0_x2.wav', y_f0_x2, fs)
    y_sp_x2 = pw.synthesize(f0, sp*2, ap, fs, pw.default_frame_period)
    sf.write('test/sp_x2.wav', y_sp_x2, fs)
    y_ap_x2 = pw.synthesize(f0, sp, ap, fs, pw.default_frame_period)
    sf.write('test/ap_x2.wav', y_ap_x2, fs)


if __name__ == "__main__":
    main()
