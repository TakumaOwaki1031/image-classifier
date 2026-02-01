import java.io.File;
import java.io.IOException;

public class BatchConverter {

    public static void main(String[] args) {
        String[] classes = {"ME", "OTHER"};
        String inputRoot = "raw/faces/";
        String outputRoot = "converted/faces/";

        for (String label : classes) {
            File inputDir = new File(inputRoot + label);
            File outputDir = new File(outputRoot + label);
            outputDir.mkdirs();

            File[] files = inputDir.listFiles((dir, name) ->
                name.toLowerCase().endsWith(".jpg") || name.toLowerCase().endsWith(".png")
            );

            if (files == null) {
                System.out.println("フォルダが見つかりません: " + inputDir.getPath());
                continue;
            }

            for (File file : files) {
                String inputPath = file.getAbsolutePath();
                String outputPath = new File(outputDir, file.getName()).getAbsolutePath();
                try {
                    ImagePreprocessor.preprocessAndSave(inputPath, outputPath);
                    System.out.println("変換完了: " + file.getName());
                } catch (IOException e) {
                    System.err.println("変換失敗: " + file.getName());
                    e.printStackTrace();
                }
            }
        }

        System.out.println("全画像の変換が完了しました。");
    }
}

