import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class ImagePreprocessor {

    public static void preprocessAndSave(String inputPath, String outputPath) throws IOException {
        BufferedImage original = ImageIO.read(new File(inputPath));
        if (original == null) {
            throw new IOException("画像が読み込めません: " + inputPath);
        }

        // 1. リサイズ（128×128, BILINEAR補間）
        BufferedImage resized = new BufferedImage(128, 128, BufferedImage.TYPE_INT_RGB);
        Graphics2D g2 = resized.createGraphics();
        g2.setRenderingHint(RenderingHints.KEY_INTERPOLATION, RenderingHints.VALUE_INTERPOLATION_BILINEAR);
        g2.drawImage(original, 0, 0, 128, 128, null);
        g2.dispose();

        // 2. 保存（JPEG）
        File output = new File(outputPath);
        ImageIO.write(resized, "jpg", output);
    }
}
