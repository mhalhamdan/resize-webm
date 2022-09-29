import cv2
import os
from exceptions import InvalidWebmFile

class WebmResizer(object):
    def __init__(self) -> None:
        pass

    def _is_filename(self, input):
        return type(input) == str 
    
    def _validate_video(self, filename: str):
        if not filename.endswith('.webm'):
            raise(InvalidWebmFile(filename))

    def _read_video(self, video_object):
        # For reading from a filename
        if self._is_filename(video_object):
            self._validate_video(video_object)
            return cv2.VideoCapture(video_object), video_object
        else:
            # TODO: reading file from bytes
            pass

    '''
    Takes either a video filename (full path) or a file like video object 
    Returns dictionary of all frames in the video wit their index
    Optional: writes images to an output directory provided in parameter
    '''
    def convert_video_to_images(self, video_object, output_dir=None) -> dict:

        video, filename = self._read_video(video_object)

        frames_dict = {}

        # Iterate
        index = 0
        while(video.isOpened()):
            ret, frame = video.read()
            if ret == False:
                break
            frames_dict[index] = frame
            index+=1
        
        # Optional: output
        if output_dir:
            # Format output path
            filename_no_ext = os.path.splitext(os.path.basename(filename))[0]
            output_path = os.path.join(output_dir, filename_no_ext)
            for index, frame in frames_dict.items():
                cv2.imwrite(f"{output_path}-{index}.jpg",frame)

        # Cleanup
        video.release()
        cv2.destroyAllWindows()

        return frames_dict



def main():

    # Example code 

    video_filename = 'examples/big-buck-bunny_trailer.webm'
    
    output_dir = "./output"

    resizer = WebmResizer()

    resizer.convert_video_to_images(video_filename, output_dir=output_dir)

if __name__ == "__main__":

    main()