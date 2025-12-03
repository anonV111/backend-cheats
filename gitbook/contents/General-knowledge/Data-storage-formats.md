### Data storage formats

Different file formats can be used to store and transfer data over the network. Text files are human-readable, so they are used for configuration files, for example. But transferring data in text formats over the network is not always rational, because they weigh more than their corresponding binary files.

-   Text formats

    -   [JSON (JavaScript Object Notation)](https://en.wikipedia.org/wiki/JSON)
        > Represents an object in which data is stored as key-value pairs.
    -   [XML (eXtensible Markup Language)](https://en.wikipedia.org/wiki/XML)
        > The format is closer to HTML. Here the data is wrapped in opening and closing tags.
    -   [YAML (Yet Another Markup Language)](https://en.wikipedia.org/wiki/YAML)
        > The format is close to markup languages like HTML. Minimalist, because it has no opening or closing tags. Easy to edit.
    -   [TOML (Tom's Obvious Minimal Language)](https://en.wikipedia.org/wiki/TOML)
        > A minimal configuration file format that's easy to read due to obvious semantics. TOML is designed to map unambiguously to a hash table. TOML should be easy to parse into data structures in a wide variety of languages.

-   Binary formats
    -   [Message Pack](https://msgpack.org/)
        > Binary analog of JSON. Allows you to pack data 15-20% more efficiently.
    -   [BSON (Binary JavaScript Object Notation)](https://en.wikipedia.org/wiki/BSON)
        > It is a superset of JSON, including additionally regular expressions, binary data and dates.
    -   [ProtoBuf (Protocol Buffers)](https://en.wikipedia.org/wiki/Protocol_Buffers)
        > Binary alternative to XML text format. Simpler, more compact and faster.

-   Image formats
    -   [JPEG (Joint Photographic Experts Group)](https://en.wikipedia.org/wiki/JPEG)
        > It is best suited for photographs and complex images with a wide range of colors. JPEG images can achieve high compression ratios while maintaining good image quality, but repeated editing and saving can result in loss of image fidelity.
    -   [PNG (Portable Network Graphics)](https://en.wikipedia.org/wiki/PNG)
        > It is a lossless compression format that supports transparency. It is commonly used for images with sharp edges, logos, icons, and images that require transparency. PNG images can have a higher file size compared to JPEG, but they retain excellent quality without degradation during repeated saves.
    -   [GIF (Graphics Interchange Format)](https://en.wikipedia.org/wiki/GIF)
        > Used for simple animations and low-resolution images with limited colors. It supports transparency and can be animated by displaying a sequence of frames.
    -   [SVG (Scalable Vector Graphics)](https://en.wikipedia.org/wiki/SVG)
        > XML-based vector image format defined by mathematical equations rather than pixels. SVG images can be scaled to any size without losing quality and are well-suited for logos, icons, and graphical elements.
    -   [WebP](https://en.wikipedia.org/wiki/WebP)
        > Modern image format developed by Google. It supports both lossy and lossless compression, providing good image quality with smaller file sizes compared to JPEG and PNG. WebP images are optimized for web use and can include transparency and animation.

-   Video formats
    -   [MP4 (MPEG-4 Part 14)](https://en.wikipedia.org/wiki/MP4_file_format)
        > Widely used video format that supports high-quality video compression, making it suitable for streaming and storing videos. MP4 files can contain both video and audio.
    -   [AVI (Audio Video Interleave)](https://en.wikipedia.org/wiki/Audio_Video_Interleave)
        > Is a multimedia container format developed by Microsoft. It can store audio and video data in a single file, allowing for synchronized playback. However, they tend to have larger file sizes compared to more modern formats.
    -   [MOV (QuickTime Movie)](https://www.adobe.com/creativecloud/video/hub/guides/what-is-an-mov-video.html)
        > Is a video format developed by Apple for use with their QuickTime media player. It is widely used with Mac and iOS devices. MOV files can contain both video and audio, and they offer good compression and quality, making them suitable for editing and professional use.
    -   [WEBM](https://en.wikipedia.org/wiki/WebM)
        > Best for videos embedded on your personal or business website. It is lightweight, load quickly and stream easily.

-   Audio formats
    -   [MP3 (MPEG-1 Audio Layer 3)](https://en.wikipedia.org/wiki/MP3)
        > The most popular audio format known for its high compression and small file sizes. It achieves this by removing some of the audio data that may be less perceptible to the human ear. Suitable for music storage, streaming, and sharing.
    -   [WAV (Waveform Audio File Format)](https://en.wikipedia.org/wiki/WAV)
        > Is an uncompressed audio format that stores audio data in a lossless manner, resulting in high-quality sound reproduction. WAV files are commonly used in professional audio production and editing due to their accuracy and fidelity. However, they tend to have larger file sizes compared to compressed formats.
    -   [AAC (Advanced Audio Coding)](https://en.wikipedia.org/wiki/Advanced_Audio_Coding)
        > Is a widely used audio format known for its efficient compression and good sound quality. It offers better sound reproduction at lower bit rates compared to MP3. AAC files are commonly used for streaming music, online radio, and mobile devices, as they deliver good audio quality while conserving bandwidth and storage.

<details>
<summary>🔗 <b>References</b></summary>

1. 📺 [**Data Formats: XML, JSON, and YAML** – YouTube](https://youtu.be/JQO-x8rzNVI)
2. 📺 [**Serialization formats: JSON and Protobuf** – YouTube](https://youtu.be/uGYZn6xk-hA)
3. 📺 [**Protocol Buffers Crash Course** – YouTube](https://youtu.be/46O73On0gyI)
4. 📺 [**Explaining Image File Formats** – YouTube](https://youtu.be/WblPwVq9KnU)
5. 📺 [**What's the difference between a JPEG, PNG, GIF, etc…?** – YouTube](https://youtu.be/ww12lImOJ38)
 </details>


