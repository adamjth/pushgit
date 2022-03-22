<?xml version="1.0" ?>
<testplan id="0000015487d1a3be762dde0d000a000a00a600f3" level="3 (Full Decoding)" name="NatGeo_Final_MXF_PGM_Production-V2">
  <description>
    
    
    
    &lt;div&gt;
                  &lt;strong&gt;Add your comments about this section here!&lt;/strong&gt;
                &lt;/div&gt;
  
  
  
  </description>
  <summary>
    Baton MXF Testplan
  </summary>
  <productVersion build="55279" major="6" minor="2" patch="0" postreleasetag="" prereleasetag=""/>
  <instructions>
    <instruction enable="false" label="Report Conformance Warnings" name="Report Conformance Warnings" override="true" section="Common" switchable="true"/>
    <instruction enable="false" label="Conformance Checks" name="ConformanceChecks" override="true" section="Common" switchable="true">
      <component complex_value_type="ConformanceChecks" label="Override Conformance Checks" name="OverrideConformanceChecks" restriction="{}" type="complex" value_format="json"/>
    </instruction>
    <instruction enable="true" label="Continue on Fatal Check Failure" name="Continue on Fatal Check Failure" override="false" section="Common" switchable="true"/>
    <instruction label="Errors" name="Errors" override="false" section="Common" switchable="false">
      <component enum="UnSupportedFormat" label="If format not supported by Baton" name="formatNotSupportedByBaton" restriction="Error" type="enumeration"/>
      <component enum="UnSupportedFormat" label="If format not supported by Test Plan" name="formatNotSupportedByTestPlan" restriction="Error" type="enumeration"/>
      <component enum="UnSupportedFormat" label="Unable to apply Track Layout/Combine All Tracks if Dolby E is detected" name="trackLayoutNotApplied" restriction="Error" type="enumeration"/>
      <component label="Maximum reporting for an error" name="maxErrorReportingLimit" restriction="v == 20" type="int_value"/>
    </instruction>
    <instruction label="Frame Rate" name="FrameRate" override="false" section="Common" switchable="false">
      <component label="Default value" name="defaultFrameRate" restriction="v == 30" type="double_value" unit="Fps"/>
    </instruction>
    <instruction enable="false" label="Selective Analysis" name="SelectiveAnalysis" override="true" section="Common" switchable="true">
      <component label="Selective Analysis" name="SelectiveAnalysisComp" restriction="{&quot;mode&quot;:&quot;partial-verification&quot;,&quot;restriction&quot;:{&quot;start&quot;:{&quot;value&quot;:0,&quot;restriction&quot;:&quot;00:00:00:00&quot;},&quot;end&quot;:{&quot;value&quot;:79380000,&quot;restriction&quot;:&quot;01:22:03:00&quot;}}}" type="SelectiveAnalysis"/>
    </instruction>
    <instruction enable="false" label="Error Filter" name="ErrorsFilter" override="true" section="Common" switchable="true">
      <component complex_value_type="ErrorsFilter" label="Error Filter" name="ErrorsFilterComp" restriction="[]" type="complex" value_format="json"/>
    </instruction>
    <instruction enable="false" label="3D Checks" name="Enable3DChecks" override="true" section="Common" switchable="true"/>
    <instruction enable="true" label="Statistical data of quality checks" name="StatisticalData" override="true" section="Common" switchable="true"/>
    <instruction enable="false" label="Content Timeline" name="ContentTimeline" override="false" section="Common" switchable="true"/>
    <instruction label="Timecodes" name="Timecodes" override="true" section="Common" switchable="false">
      <component label="Show Actual Timecodes" name="showActualTimecodes" restriction="true" type="boolean"/>
    </instruction>
    <instruction enable="false" label="Related audio/video files" name="RelatedFiles" override="true" section="Common" switchable="true">
      <component label="Pattern" name="Pattern" restriction="" type="string"/>
    </instruction>
    <instruction label="Dolby E" name="DolbyE" override="false" section="AudioEncoding" switchable="false">
      <component label="Auto Detect" name="AutoDetect" restriction="true" type="boolean"/>
      <component label="Bytes to ignore" name="IgnoredBytes" restriction="v == 102400" type="int_value" unit="Bytes"/>
      <component label="Dolby E and Stereo on a single track" name="DetectStereoNDolbyE" restriction="false" type="boolean"/>
    </instruction>
    <instruction enable="false" label="Prefer User specified Channel Assignment over metadata" name="OverrideAudioChannelAssignment" override="false" section="AudioEncoding" switchable="true"/>
    <instruction label="Audio Channel Assignment" name="AudioChannelLayout" override="false" section="AudioEncoding" switchable="false">
      <component complex_value_type="AudioChannelLayout" label="AudioChannelLayout" name="AudioChannelLayout" restriction="[]" type="complex" value_format="json"/>
    </instruction>
    <instruction label="Black level" name="BlackLevelSettings" override="true" section="UncompressedVideo" switchable="false">
      <component label="Minimum Luma Value" name="MinYVal" restriction="v == 0" type="int_value"/>
      <component label="Maximum Luma Value" name="MaxYVal" restriction="v == 35" type="int_value"/>
      <component label="Minimum Chroma(Cb) Value" name="MinCbVal" restriction="v == 120" type="int_value"/>
      <component label="Maximum Chroma(Cb) Value" name="MaxCbVal" restriction="v == 135" type="int_value"/>
      <component label="Minimum Chroma(Cr) Value" name="MinCrVal" restriction="v == 120" type="int_value"/>
      <component label="Maximum Chroma(Cr) Value" name="MaxCrVal" restriction="v == 135" type="int_value"/>
    </instruction>
    <instruction label="Black Frames" name="BlackFrames" override="true" section="UncompressedVideo" switchable="false">
      <component label="Minimum Duration" name="MinimumDuration" restriction="v == 250" type="double_value" unit="Milli Seconds"/>
    </instruction>
    <instruction label="Freeze and Duplicate Frames" name="FreezeFrames" override="true" section="UncompressedVideo" switchable="false">
      <component label="Min Freeze Frames duration" name="MinimumDuration" restriction="v == 250" type="double_value" unit="Milli Seconds"/>
      <component label="Maximum dissimilar pixels" name="MaximumPercentage" restriction="v == 1" type="double_value" unit="Percent"/>
    </instruction>
    <instruction label="Video Signal Level Cap Values" name="SignalLevelCapValues" override="true" section="UncompressedVideo" switchable="false">
      <component complex_value_type="VideoSignalCapLevels" label="Video Signal Level Cap Values" name="SignalLevelCapValues" restriction="[{&quot;yuv&quot;:{&quot;bitdepth&quot;:8,&quot;ymin&quot;:0,&quot;ymax&quot;:255,&quot;cbmin&quot;:0,&quot;cbmax&quot;:255,&quot;crmin&quot;:0,&quot;crmax&quot;:255}}]" type="complex" value_format="json"/>
    </instruction>
    <instruction label="Black Bars" name="BlackBars" override="true" section="UncompressedVideo" switchable="false">
      <component label="Exclude Black Bars" name="excludeInQualityChecks" restriction="false" type="boolean"/>
    </instruction>
    <instruction label="Thumbnails" name="Thumbnails" override="true" section="UncompressedVideo" switchable="false">
      <component label="Thumbnail dumping interval" name="thumbnailDumpingInterval" restriction="v == 60000" type="int_value" unit="Milli Seconds"/>
      <component label="Number of thumbnails before and after a pictures with errors" name="thumbnailsAroundErrors" restriction="v == 0" type="int_value" unit="Pictures"/>
      <component label="Large thumbnails for quality issues" name="largeThumbnails" restriction="false" type="boolean"/>
      <component label="Mark Regions for quality issues" name="showRegions" restriction="false" type="boolean"/>
      <component label="Mark Regions for Baton Media Player" name="showRegionsInPlayer" restriction="false" type="boolean"/>
    </instruction>
    <instruction enable="false" label="VBI Settings" name="VBISettings" override="true" section="UncompressedVideo" switchable="true">
      <component complex_value_type="VBISettings" label="VBI Settings" name="VBISettingsComp" restriction="[]" type="complex" value_format="json"/>
    </instruction>
    <instruction label="Motion Jerk" name="MotionJerk" override="true" section="UncompressedVideo" switchable="false">
      <component enum="MotionJerkTypes" label="Check Motion Jerk" name="MotionJerkType" restriction="ProgressiveJerk,MotionJitter,ReverseFieldDominance,PulldownJudder" type="enumeration"/>
    </instruction>
    <instruction label="Deinterlacing" name="Deinterlacing" override="true" section="UncompressedVideo" switchable="false">
      <component label="Apply Deinterlacing before quality checking" name="ApplyDeinterlacing" restriction="false" type="boolean"/>
      <component enum="DeinterlacingMethods" label="Deinterlacing Method" name="DeinterlacingMethod" restriction="Mean" type="enumeration"/>
    </instruction>
    <instruction enable="false" label="Video Quality" name="VideoQualitySettings" override="true" section="UncompressedVideo" switchable="true">
      <component complex_value_type="IncludeExcludeRegions" label="Region" name="VideoQualityRegions" restriction="[]" type="complex" value_format="json"/>
    </instruction>
    <instruction label="Text Detection" name="TextDetection" override="true" section="UncompressedVideo" switchable="false">
      <component label="Exclude Text Regions" name="excludeTextInQualityChecks" restriction="false" type="boolean"/>
    </instruction>
    <instruction enable="false" label="Fine Video Quality Analysis for 4K Video" name="FineAnalysis" override="true" section="UncompressedVideo" switchable="true"/>
    <instruction enable="false" label="Dump Text Information (Closed Captions/Subtitles)" name="DumpTextInfo" override="true" section="Subtitle" switchable="true"/>
    <instruction label="Program Loudness" name="AudioProgramLoudness" override="false" section="UncompressedAudio" switchable="false">
      <component enum="ProgramLoudnessMode" label="Mode" name="PLMode" restriction="Level Gating" type="enumeration"/>
      <component label="Speech Content" name="PLSpeechContent" restriction="v == 80" type="int_value" unit="%"/>
      <component label="Short Form Content Duration" name="PLSFCD" restriction="v == 60000" type="duration_value"/>
    </instruction>
    <instruction label="Loudness" name="AudioLoudness" override="false" section="UncompressedAudio" switchable="false">
      <component enum="LoudnessSpecifications" label="Specification" name="LoudnessSpecification" restriction="BS-1770-3" type="enumeration"/>
      <component label="Use DPLM Technology" name="DPLMTechnology" restriction="false" type="boolean"/>
    </instruction>
    <instruction label="Master File" name="MasterFilePattern" override="true" section="UncompressedAudio" switchable="false">
      <component label="Pattern" name="Pattern" restriction="" type="string"/>
    </instruction>
    <instruction enable="false" label="Ignore Mute Tracks" name="IgnoreMuteTracks" override="false" section="UncompressedAudio" switchable="true"/>
    <instruction enable="false" label="Automatic Start of Media Detection" name="SOMDetection" override="false" section="UncompressedAudio" switchable="true"/>
    <instruction label="Test Tone" name="TestTone" override="false" section="UncompressedAudio" switchable="false">
      <component label="Minimum Duration" name="MinimumDuration" restriction="v == 2000" type="extended_duration_value" unit="msecs"/>
    </instruction>
    <instruction label="Phase Mismatch" name="PhaseMismatch" override="false" section="UncompressedAudio" switchable="false">
      <component label="Minimum Duration" name="MinimumDuration" restriction="v == 2000" type="extended_duration_value" unit="msecs"/>
    </instruction>
    <instruction enable="false" label="Override Audio Track Layout" name="OverrideAudioTrackLayout" override="false" section="ContainerEncoding" switchable="true"/>
    <instruction label="Audio Track Layout" name="AudioTrackLayout" override="true" section="ContainerEncoding" switchable="false">
      <component complex_value_type="AudioTrackLayout" label="AudioTrackLayout" name="AudioTrackLayout" restriction="[{&quot;count&quot;:8,&quot;tracks&quot;:[{&quot;size&quot;:6,&quot;ig&quot;:false,&quot;doblye&quot;:false,&quot;channels&quot;:{&quot;0&quot;:&quot;L&quot;,&quot;1&quot;:&quot;R&quot;,&quot;2&quot;:&quot;C&quot;,&quot;3&quot;:&quot;LFE&quot;,&quot;4&quot;:&quot;SL&quot;,&quot;5&quot;:&quot;SR&quot;},&quot;languages&quot;:[]},{&quot;size&quot;:2,&quot;ig&quot;:false,&quot;doblye&quot;:false,&quot;channels&quot;:{&quot;0&quot;:&quot;L&quot;,&quot;1&quot;:&quot;R&quot;},&quot;languages&quot;:[]}]}]" type="complex" value_format="json"/>
    </instruction>
    <instruction label="Audio Program Configuration" name="AudioProgramConfiguration" override="false" section="ContainerEncoding" switchable="false">
      <component complex_value_type="AudioProgramConfiguration" label="AudioProgramConfiguration" name="AudioProgramConfiguration" restriction="[]" type="complex" value_format="json"/>
    </instruction>
    <instruction enable="false" label="Combine All Tracks" name="CombineAllTracks" override="false" section="ContainerEncoding" switchable="true"/>
    <instruction label="Content Layout" name="Content Layout" override="true" section="ContainerEncoding" switchable="false">
      <component label="Tolerance Duration" name="tolerance" restriction="v == 0" type="duration_value" unit="msec"/>
      <component label="Tolerance Duration" name="tolerance_frames" restriction="v == 0" type="int_value" unit="frames"/>
    </instruction>
    <instruction label="Define Slate Layout" name="SlateLayout" override="true" section="ContainerEncoding" switchable="false">
      <component complex_value_type="SlateLayout" label="Slate Layout" name="Slate Layout" restriction="{}" type="complex" value_format="json"/>
    </instruction>
    <instruction enable="false" label="Analyze Sidecar Captions/Subtitles" name="AnalyzeSubtitlesWithMedia" override="true" section="Subtitle" switchable="true"/>
    <instruction enable="false" label="Digital Cinema Package Compliance" name="Digital Cinema Package Compliance" override="true" section="MXF" switchable="true"/>
    <instruction enable="false" label="AS-02 Compliance" name="AS02 Compliance" override="true" section="MXF" switchable="true"/>
    <instruction enable="false" label="AS-11 Compliance" name="AS11 Compliance" override="true" section="MXF" switchable="true"/>
    <instruction enable="false" label="AS-03 Compliance" name="AS03 Compliance" override="true" section="MXF" switchable="true"/>
    <instruction enable="false" label="ARD_ZDF_HDF Compliance" name="IRTCompliance" override="true" section="MXF" switchable="true"/>
    <instruction enable="false" label="DPP Compliance" name="DPPCompliance" override="true" section="MXF" switchable="true"/>
    <instruction enable="false" label="RDD25 Compliance" name="RDD25Compliance" override="true" section="MXF" switchable="true"/>
    <instruction enable="false" label="Sony XDCAM Compliance" name="SonyXDCAMCompliance" override="true" section="MXF" switchable="true"/>
    <instruction label="Default MPEG-2 Color Space" name="MPEG2ColorSpace" override="true" section="MPEG2Video" switchable="false">
      <component enum="MPEG2ColorSpaceType" label="Default MPEG-2 Color Space" name="MPEG2ColorSpace" restriction="709" type="enumeration"/>
    </instruction>
  </instructions>
  <configurations>
    <fileConfigurations>
      <configuration category="MXF" name="MXF" type="container">
        <sectionReferences>
          <reference category="ContainerEncoding" name="Common" type="section"/>
          <reference category="MXF" name="Common" type="section"/>
        </sectionReferences>
        <defaultESConfigurations>
          <reference category="MPEG2Video" name="MXF-MPEG2Video" type="configuration"/>
          <reference category="AES3Audio" name="MXF-AES3Audio" type="configuration"/>
          <reference category="BWFAudio" name="MXF-BWFAudio" type="configuration"/>
          <reference category="LPCMAudio" name="MXF-LPCMAudio" type="configuration"/>
          <reference category="Subtitle" name="MXF-Subtitle" type="configuration"/>
          <reference category="ANC" name="MXF-ANC" type="configuration"/>
        </defaultESConfigurations>
        <ESConfigurations/>
      </configuration>
    </fileConfigurations>
    <elementaryConfigurations>
      <configuration category="AES3Audio" name="MXF-AES3Audio" type="elementary">
        <sectionReferences>
          <reference category="AudioEncoding" name="Common" type="section"/>
          <reference category="UncompressedAudio" name="Common" type="section"/>
        </sectionReferences>
      </configuration>
      <configuration category="ANC" name="MXF-ANC" type="elementary">
        <sectionReferences>
          <reference category="ClosedCaption" name="Common" type="section"/>
        </sectionReferences>
      </configuration>
      <configuration category="BWFAudio" name="MXF-BWFAudio" type="elementary">
        <sectionReferences>
          <reference category="AudioEncoding" name="Common" type="section"/>
          <reference category="UncompressedAudio" name="Common" type="section"/>
          <reference category="BWFAudio" name="Common" type="section"/>
        </sectionReferences>
      </configuration>
      <configuration category="LPCMAudio" name="MXF-LPCMAudio" type="elementary">
        <sectionReferences>
          <reference category="AudioEncoding" name="Common" type="section"/>
          <reference category="UncompressedAudio" name="Common" type="section"/>
          <reference category="LPCMAudio" name="Common" type="section"/>
        </sectionReferences>
      </configuration>
      <configuration category="MPEG2Video" name="MXF-MPEG2Video" type="elementary">
        <sectionReferences>
          <reference category="VideoEncoding" name="Common" type="section"/>
          <reference category="UncompressedVideo" name="Common" type="section"/>
          <reference category="Uncompressed3DVideo" name="Common" type="section"/>
          <reference category="MPEG2Video" name="Common" type="section"/>
          <reference category="ClosedCaption" name="Common" type="section"/>
          <reference category="Subtitle" name="Common" type="section"/>
          <reference category="BurntInText" name="Common" type="section"/>
        </sectionReferences>
      </configuration>
      <configuration category="Subtitle" name="MXF-Subtitle" type="elementary">
        <sectionReferences>
          <reference category="Subtitle" name="Common" type="section"/>
        </sectionReferences>
      </configuration>
    </elementaryConfigurations>
  </configurations>
  <sections>
    <section category="Uncompressed3DVideo" label="3D Video Quality" name="Common" summary="3D Video Quality Features">
      <description>
        
        
        
        3D Video Quality Features
      
      
      
      </description>
    </section>
    <section category="AudioEncoding" label="Audio Description" name="Common" summary="Audio Description Features">
      <description>
        
        
        
        
        Audio Description Features
      
      
      
      
      </description>
      <item check="true" index="0" label="Bits per sample" level="1" log="true" name="Bits per sample" severity="Serious">
        <component check="true" enum="NumBitsPerSample" name="Bits per sample" restriction="16,24" rule="!=" type="enumeration"/>
      </item>
      <item index="0" label="Channel Configuration" level="1" log="true" name="Channel Configuration"/>
      <item check="false" index="0" label="Frame Size" level="1" name="Frame Size" severity="Serious"/>
      <item check="false" index="0" label="LFE Channels" level="1" log="true" name="LFE Channels" severity="Serious"/>
      <item check="false" index="0" label="Duration" level="1" log="true" name="Duration" severity="Serious"/>
      <item index="0" label="Audio Channels" level="1" name="Audio Channels" severity="Serious">
        <component check="false" label="Audio Channels" log="true" name="Audio Channels" restriction="" type="integer"/>
        <component check="true" label="Audio Channel Change detected" log="false" name="Audio Channels Change"/>
      </item>
      <item index="0" label="Bit Rate" level="1" name="Bit Rate" severity="Serious">
        <component check="false" label="Bit Rate" log="true" name="Bit Rate" restriction="" type="integer" unit="Kbps"/>
        <component check="true" label="Bit Rate Change detected" log="false" name="Bit Rate Change"/>
      </item>
      <item index="0" label="Sampling Frequency" level="1" name="Sampling Frequency" severity="Serious">
        <component check="true" label="Sampling Frequency" log="true" name="Sampling Frequency" restriction="v != 48000" type="integer" unit="Hz"/>
        <component check="true" label="Sampling Frequency Change detected" log="false" name="Sampling Frequency Change"/>
      </item>
    </section>
    <section category="VideoEncoding" label="Video Description" name="Common" summary="Video Description Features">
      <description>
        
        
        
        
        Video Description Features
      
      
      
      
      </description>
      <item check="false" index="0" label="Closed Captions" level="1" log="false" name="ClosedCaptions" severity="Serious"/>
      <item check="true" index="0" label="Chroma Format" level="1" log="true" name="Chroma Format" severity="Serious">
        <component check="true" enum="ChromaFormat" name="Chroma Format" restriction="4:2:2" rule="!=" type="enumeration"/>
      </item>
      <item check="false" index="0" label="SMPTE 2052" level="1" log="false" name="SMPTE 2052" severity="Serious"/>
      <item check="false" index="0" label="Frame Rate" level="1" log="true" name="Frame Rate" severity="Serious"/>
      <item check="false" index="0" label="Active Pixels" level="3" log="true" name="Active Pixels" severity="Serious"/>
      <item index="0" label="Active Format" level="1" name="Active Format" severity="Serious">
        <component check="false" label="AFD Change detected" log="false" name="AFD Change"/>
        <component check="false" label="AFD missing" name="AFD Info"/>
        <component check="true" enum="ActiveFormatTypes" label="Active Format" log="true" name="Active Format" restriction="16:9 [centre][1010],16:9 [with shoot and protect 4:3 centre][1111]" rule="!=" type="enumeration"/>
      </item>
      <item index="0" label="Bitrate" level="1" name="Average Bitrate" severity="Serious">
        <component check="false" label="Average Bitrate" log="true" name="Average Bitrate" type="double"/>
        <component check="false" label="Instantaneous Bitrate" log="false" name="InstantaneousBitrate" type="double"/>
        <component label="Interval for Instantaneous Bitrate" name="WindowSize" restriction="v == 1" type="integer" unit="secs"/>
      </item>
      <item check="false" index="0" label="Duration" level="1" log="true" name="Duration" severity="Serious">
        <component check="false" label="Duration" name="Duration" type="extended_duration"/>
      </item>
      <item check="true" index="0" label="Scan Order" level="1" log="true" name="Scan Order" severity="Serious">
        <component check="true" enum="ScanOrderMode" label="Scan Order" name="Scan Order" restriction="Top field first" rule="!=" type="enumeration"/>
      </item>
      <item index="0" label="Resolution" level="1" name="Resolution" severity="Serious">
        <component check="false" complex_value_type="VideoResolution" label="Resolution" log="true" name="NewResolution" restriction="" rule="!=" type="complex" value_format="json"/>
        <component check="true" label="Resolution Change detected" log="true" name="Resolution Change"/>
      </item>
      <item check="false" index="0" label="Bits Per Pixel" level="1" log="true" name="Bits Per Sample" severity="Serious"/>
      <item check="false" index="0" label="Pixel Aspect Ratio" level="1" log="true" name="Sample Aspect Ratio" severity="Serious"/>
      <item check="true" index="0" label="Display Aspect Ratio" level="1" log="true" name="Display Aspect Ratio" severity="Serious">
        <component check="true" complex_value_type="VideoDAR" label="DAR" name="NewDAR" restriction="[&quot;16:9&quot;]" rule="!=" type="complex" value_format="json"/>
        <component label="Exclude Black Bars" name="excludeInDAR" restriction="false" type="boolean"/>
      </item>
      <item index="0" label="Video Format" level="1" name="Video Format" severity="Serious">
        <component check="false" enum="VideoFormat" label="Video Format" log="true" name="Video Format" restriction="" rule="!=" type="enumeration"/>
        <component check="false" label="Video Format Change detected" log="false" name="Video Format Change"/>
      </item>
      <item index="0" label="Picture Scanning Type" level="1" name="Picture Scanning Type" severity="Serious">
        <component check="true" enum="ScanningType" label="Picture Scanning Type" log="true" name="Picture Scanning Type" restriction="Progressive" rule="!=" type="enumeration"/>
        <component check="false" label="Picture Scanning Type Change detected" log="false" name="Picture Scanning Type Change"/>
      </item>
      <item index="0" label="Cadence Pattern" level="1" name="Cadence" severity="Serious">
        <component check="false" label="Cadence Pattern Change detected" log="false" name="Cadence Change"/>
        <component check="false" complex_value_type="VideoCadencePattern" label="Cadence Pattern" log="true" name="CadencePattern" restriction="" rule="!=" type="complex" value_format="json"/>
      </item>
      <item check="false" index="0" label="GOP Structure" level="1" log="true" name="GOP Structure" severity="Serious">
        <component check="false" label="Average GOP Length" name="AvgGOPLength" restriction="" type="integer" unit="Frames"/>
        <component check="false" complex_value_type="GOPMN" label="M and N" name="GOPMNComp" restriction="" rule="!=" type="complex" value_format="json"/>
        <component label="Ignore Error Count" name="Ignore Error Count" restriction="v == 0" type="integer"/>
      </item>
      <item index="0" label="Color Information" level="1" name="Color Information" severity="Serious">
        <component check="false" enum="ColorMatrix" label="Color Matrix" log="true" name="Color Matrix" restriction="" rule="!=" type="enumeration"/>
        <component check="false" enum="ColorPrimaries" label="Color Primaries" log="false" name="Color Primaries" restriction="" rule="!=" type="enumeration"/>
        <component check="false" enum="TransferCharacteristics" label="Transfer Characteristics" log="false" name="Transfer Characteristics" restriction="" rule="!=" type="enumeration"/>
      </item>
      <item index="0" label="Quantization Parameter" level="1" name="QuantizationParameter" severity="Serious">
        <component check="false" label="Quantization Parameter" log="false" name="QuantizationParameter" type="integer"/>
        <component check="false" label="Quantization Parameter Change" name="QuantizationParameterChange" type="integer"/>
      </item>
    </section>
    <section category="UncompressedVideo" label="Video Quality" name="Common" summary="Video Quality Features">
      <description>
        
        
        
        
        Video Quality Features
      
      
      
      
      </description>
      <item check="false" index="0" label="Color Bar" level="3" log="true" name="Color Bars" severity="Serious">
        <component label="Check Color Bar during video" name="Color Bar During video" restriction="true" type="boolean"/>
        <component label="Select Custom Color Bar Image" name="CustomColorBarImage" type="image"/>
        <component label="Acceptable deviation" name="Deviation" restriction="v == 5" type="double_value" unit="Percent"/>
        <component check="false" label="Duration" name="Duration in Beginning" restriction="" type="extended_duration"/>
        <component check="false" enum="ColorBarType" label="Color Bar type" name="Type" restriction="" rule="!=" type="enumeration"/>
      </item>
      <item check="false" index="0" label="Blockiness" level="3" multiple="true" name="Blockiness" severity="Serious"/>
      <item check="false" index="0" label="Ringing Artifacts" level="3" multiple="true" name="Ringing Artifacts" severity="Serious"/>
      <item check="false" index="0" label="Mosquito Noise" level="3" multiple="true" name="Mosquito Noise" severity="Serious"/>
      <item check="false" index="0" label="Blurriness" level="3" multiple="true" name="Blurriness" severity="Serious"/>
      <item check="false" index="0" label="Black Bars" level="3" log="false" name="Black Bars" severity="Serious"/>
      <item index="0" label="Black Frames" level="3" multiple="true" name="Black Frames" severity="Serious">
        <component check="false" label="Black Frames during the video" name="During the Video" restriction="" type="extended_duration"/>
        <component check="true" label="Black Frames in Lead-in" name="Lead-in" restriction="v &lt; 2" type="extended_duration" unit="frames"/>
        <component check="true" label="Black Frames in Lead-out" name="Lead-out" restriction="v &lt; 2000" type="extended_duration"/>
      </item>
      <item index="1" label="Black Frames" level="3" multiple="true" name="Black Frames" severity="Info">
        <component check="true" label="Black Frames during the video" name="During the Video" restriction="v &lt; 5000" type="extended_duration"/>
        <component check="false" label="Black Frames in Lead-in" name="Lead-in" restriction="" type="extended_duration"/>
        <component check="false" label="Black Frames in Lead-out" name="Lead-out" restriction="" type="extended_duration"/>
      </item>
      <item check="false" index="0" label="Brightness" level="3" log="false" name="Brightness" severity="Serious"/>
      <item check="false" index="0" label="Contrast" level="3" log="false" multiple="true" name="Contrast" severity="Serious"/>
      <item check="false" index="0" label="Video Signal Level" level="3" log="false" multiple="true" name="Video Signal Levels" severity="Serious"/>
      <item check="false" index="0" label="RGB Color Gamut" level="3" multiple="true" name="RGB Color Gamut" severity="Serious"/>
      <item check="false" index="0" label="Combing Artifact" level="3" multiple="true" name="Edge Jagginess" severity="Serious"/>
      <item index="0" label="Chroma Change" level="3" name="Chroma Change" severity="Serious">
        <component check="false" label="Channel Swap Detected" name="ChannelSwap"/>
        <component check="false" label="Color Change Detected" name="ColorChange"/>
        <component check="false" label="Color Inversion Detected" name="ColorInversion"/>
        <component check="false" label="Color Loss/Gain Detected" name="ColorLossGain"/>
      </item>
      <item check="false" index="0" label="White Point" level="3" log="false" name="White Point" severity="Serious"/>
      <item check="false" index="0" label="Halfline Blanking" level="3" name="HalflineBlanking" severity="Serious"/>
      <item check="false" index="0" label="Pattern Noise" level="3" name="PatternNoise" severity="Serious"/>
      <item check="false" index="0" label="Freeze Frames" level="3" multiple="true" name="Freeze Frames" severity="Serious"/>
      <item check="false" index="0" label="Duplicate Frames" level="3" name="Duplicate Frames" severity="Serious"/>
      <item check="false" index="0" label="Ghosting Artifact" level="3" name="Ghosting Artifact" severity="Serious"/>
      <item check="false" index="0" label="Shot Transition" level="3" multiple="true" name="Shot Transition" severity="Serious"/>
      <item check="false" index="0" label="Field Dominance Error" level="3" name="Field Dominance Error" severity="Serious"/>
      <item check="false" index="0" label="Motion Jerk" level="3" log="false" name="Motion Jerk" severity="Serious">
        <component enum="FieldOrderType" label="Field Display Order" name="Field Order Type" restriction="Automatic" rule="==" type="enumeration"/>
        <component check="false" label="Motion Jerk detected" name="MotionJerkPresent"/>
      </item>
      <item index="0" label="Telecine" level="3" name="Cadence Break" severity="Serious">
        <component check="false" complex_value_type="VideoCadencePattern" label="Cadence Pattern" log="false" name="Cadence" restriction="" rule="!=" type="complex" value_format="json"/>
        <component check="false" label="Cadence Pattern Change Detected" log="false" name="Cadence Change"/>
      </item>
      <item check="false" index="0" label="Upconversion" level="3" multiple="true" name="Upconversion" severity="Serious"/>
      <item check="false" index="0" label="Color Banding" level="3" name="ColorBanding" severity="Serious"/>
      <item check="false" index="0" label="Field Order" level="3" log="false" name="Field Order" severity="Serious"/>
      <item check="false" index="0" label="Dropout" level="3" multiple="true" name="Video Dropout" severity="Serious"/>
      <item check="false" index="0" label="Defective Pixel" level="3" name="Defective Pixel" severity="Serious"/>
      <item check="false" index="0" label="Film Grain Noise" level="3" log="false" name="Video Noise" severity="Serious"/>
      <item check="false" index="0" label="Analog Noise" level="3" name="AnalogNoise" severity="Serious"/>
      <item check="false" index="0" label="High Frequency Noise" level="3" name="HFNoise" severity="Serious"/>
      <item check="false" index="0" label="Moire Pattern" level="3" name="Moire Pattern" severity="Serious"/>
      <item check="false" index="0" label="PSE Video Flash" level="3" name="Flashy Video" severity="Serious">
        <component enum="FlashinessSensitivity" label="Spatial Pattern Detection" name="Flashiness_Sensitivity" restriction="Low Sensitivity" rule="==" type="enumeration"/>
        <component check="false" label="PSE Video Flash detected" name="VideoFlashesDetected"/>
      </item>
      <item check="false" index="0" label="Pixelation" level="3" multiple="true" name="Pixelation" severity="Serious"/>
      <item check="false" index="0" label="Image Presence" level="3" name="Image Matcher" severity="Serious"/>
      <item index="0" label="Credits" level="3" name="Credit Detection" severity="Serious">
        <component label="Bottom Margin" name="Bottom Margin" restriction="v == 20" type="int_value" unit="Percent"/>
        <component label="Acceptable Margin deviation" name="Deviation" restriction="v == 10" type="int_value" unit="Percent"/>
        <component label="Left Margin" name="Left Margin" restriction="v == 20" type="int_value" unit="Percent"/>
        <component check="false" enum="Presence" label="Credits" log="false" name="Presence" restriction="" rule="==" type="enumeration"/>
        <component label="Right Margin" name="Right Margin" restriction="v == 20" type="int_value" unit="Percent"/>
        <component check="false" label="Credits present out of title safe area" name="Title Safe Area"/>
        <component label="Top Margin" name="Top Margin" restriction="v == 20" type="int_value" unit="Percent"/>
      </item>
      <item check="false" index="0" label="Action Safe Area" level="3" name="ActionSafeArea" severity="Serious"/>
      <item check="false" index="0" label="Blank Frames" level="3" name="Blank Frames" severity="Serious"/>
    </section>
    <section category="LPCMAudio" label="LPCM Audio" name="Common" summary="LPCM Audio Features">
      <description>
        
        
        
        LPCM Audio Features
      
      
      
      </description>
      <item check="false" index="0" label="Endianness" level="1" log="true" name="Endianness" severity="Serious"/>
    </section>
    <section category="ClosedCaption" label="ClosedCaption" name="Common" summary="Closed Caption">
      <description>
        
        
        
        Closed Caption
      
      
      
      </description>
      <item check="false" index="0" label="Dropout" level="1" name="Dropout" severity="Warning">
        <component enum="AllCCServices" label="Check Dropout in " name="CCServicesDropoutCheck" restriction="CC1,CC3,ID1,ID2" rule="==" type="enumeration"/>
        <component check="false" label="Dropout" name="Dropout" restriction="" type="extended_duration"/>
      </item>
      <item check="false" index="0" label="Profane Words" level="1" log="false" name="ProfaneWords" severity="Serious">
        <component check="false" enum="PresentTypes" label="Profane Words" name="ProfaneWords" restriction="" rule="==" type="enumeration"/>
        <component label="Select Profane Words Dictionary" name="ProfaneWordsDictionary" restriction="All" type="ProfaneWordGroup"/>
      </item>
      <item check="true" index="0" label="Closed Caption 608 Data" level="1" log="true" name="ClosedCaption608" severity="Warning">
        <component check="true" enum="PresentTypes" label="Closed Caption 608 Data" name="ClosedCaption608" restriction="Present" rule="!=" type="enumeration"/>
      </item>
      <item check="false" index="0" label="CC608 Services" level="1" log="true" name="CC608 Services" severity="Warning">
        <component check="false" label="CC608 Services" name="CC608 Services" type="enumeration"/>
      </item>
      <item check="false" index="0" label="CC608 Service Count" level="1" log="true" name="CC608 Service Count" severity="Warning">
        <component check="false" label="CC608 Service Count" name="CC608 Service Count" type="integer"/>
      </item>
      <item check="true" index="0" label="CC608 Validity" level="1" log="true" name="CC608Validity" severity="Serious">
        <component check="true" enum="PresentTypes" label="Valid CC608 data" name="CC608Validity" restriction="Present" rule="!=" type="enumeration"/>
      </item>
      <item check="false" index="0" label="CC608 Language" level="1" log="true" name="CC608Language" severity=""/>
      <item check="false" index="0" label="CC608 Paint Style" level="1" log="true" name="CC608PaintStyle" severity="Warning">
        <component label="Check only first paint style" name="608PaintStyleReportingRule" restriction="false" type="boolean"/>
        <component check="false" label="CC608 Paint Style" name="CC608PaintStyle" type="enumeration"/>
      </item>
      <item check="true" index="0" label="Closed Caption 708 Data" level="1" log="true" name="ClosedCaption708" severity="Warning">
        <component check="true" enum="PresentTypes" label="Closed Caption 708 Data" name="ClosedCaption708" restriction="Present" rule="!=" type="enumeration"/>
      </item>
      <item check="false" index="0" label="CC708 Services" level="1" log="true" name="CC708 Services" severity="Warning">
        <component check="false" label="CC708 Services" name="CC708 Services" type="enumeration"/>
      </item>
      <item check="false" index="0" label="CC708 Service Count" level="1" log="true" name="CC708 Service Count" severity="Warning">
        <component check="false" label="CC708 Service Count" name="CC708 Service Count" type="integer"/>
      </item>
      <item check="true" index="0" label="CC708 Validity" level="1" log="true" name="CC708Validity" severity="Warning">
        <component check="true" enum="PresentTypes" label="Valid CC708 data" name="CC708Validity" restriction="Present" rule="!=" type="enumeration"/>
      </item>
      <item check="false" index="0" label="CC708 Language" level="1" log="true" name="CC708Language" severity=""/>
      <item check="false" index="0" label="CC708 Paint Style" level="1" log="true" name="CC708PaintStyle" severity="Warning">
        <component label="Check only first paint style" name="708PaintStyleReportingRule" restriction="false" type="boolean"/>
        <component check="false" label="CC708 Paint Style" name="CC708PaintStyle" type="enumeration"/>
      </item>
      <item check="false" index="0" label="Program Name" level="1" log="false" name="Program Name" severity="Serious">
        <component check="false" label="Program Name" name="Program Name" type="string"/>
      </item>
      <item index="0" label="Program Rating" level="1" name="ProgramRating" variants="US-TV">
        <variant check="false" label="US TV Parental Guidelines" log="true" name="US-TV" severity="Warning">
          <component enum="USTVContentLabels" label="Content Label" name="USTVContentLabel" restriction="" rule="!=" type="enumeration"/>
          <component enum="USTVProgramRatingTypes" label="Program Rating" name="USTVRating" restriction="" rule="!=" type="enumeration"/>
        </variant>
      </item>
      <item check="false" index="0" label="CGMS-A" level="1" log="false" name="CGMS A" severity="Serious">
        <component check="false" label="CGMS-A" name="CGMS A" type="enumeration"/>
      </item>
      <item check="false" index="0" label="TimeCode Type" level="1" log="false" name="TimeCodeType" severity="Serious"/>
    </section>
    <section category="BurntInText" label="Burnt In Text" name="Common" summary="Burnt In Text Features">
      <description>
        
        
        
        Burnt In Text Features
      
      
      
      </description>
      <item index="0" label="Subtitles" level="3" name="Subtitle Detection" severity="Serious">
        <component label="Bottom Margin" name="Bottom Margin" restriction="v == 20" type="int_value" unit="Percent"/>
        <component label="Maximum Bounding Box" log="false" name="BoundingBox"/>
        <component label="Color" log="false" name="Color"/>
        <component label="Subtitle Area Deviation" name="Deviation" restriction="v == 10" type="int_value" unit="Percent"/>
        <component check="false" enum="SubTitleLanguages" label="Language" log="false" name="Language" restriction="" rule="!=" type="enumeration"/>
        <component label="Left Margin" name="Left Margin" restriction="v == 20" type="int_value" unit="Percent"/>
        <component check="false" enum="Presence" label="Subtitles" log="true" name="Presence" restriction="" rule="==" type="enumeration"/>
        <component label="Right Margin" name="Right Margin" restriction="v == 20" type="int_value" unit="Percent"/>
        <component check="false" label="Subtitles present out of the subtitles area" name="Subtitle Area"/>
        <component label="Top Margin" name="Top Margin" restriction="v == 20" type="int_value" unit="Percent"/>
      </item>
    </section>
    <section category="UncompressedAudio" label="Audio Quality" name="Common" summary="Audio Quality Features">
      <description>
        
        
        
        
        Audio Quality Features
      
      
      
      
      </description>
      <item index="0" label="Silence" level="3" multiple="true" name="Silence" severity="Serious">
        <component complex_value_type="SilenceDetectionMode" label="Detection Mode" name="Detection Mode" restriction="{&quot;type&quot;:&quot;Cumulative&quot;}" rule="==" type="complex" value_format="json"/>
        <component check="false" label="Silence during the audio" name="During the Audio" restriction="" type="extended_duration_audio"/>
        <component check="false" label="Silence in lead-in" name="Lead-in" restriction="v &lt; 2" type="extended_duration_audio"/>
        <component check="false" label="Silence in lead-out" name="Lead-out" restriction="v &lt; 2000" type="extended_duration_audio"/>
        <component check="false" label="Mute audio detected" name="MuteTrackFound"/>
      </item>
      <item index="1" label="Silence" level="3" multiple="true" name="Silence" severity="Info">
        <component complex_value_type="SilenceDetectionMode" label="Detection Mode" name="Detection Mode" restriction="{&quot;type&quot;:&quot;Cumulative&quot;}" rule="==" type="complex" value_format="json"/>
        <component check="true" label="Silence during the audio" name="During the Audio" restriction="v &lt; 2000" type="extended_duration_audio"/>
        <component check="true" label="Silence in lead-in" name="Lead-in" restriction="v &lt; 2" type="extended_duration_audio"/>
        <component check="true" label="Silence in lead-out" name="Lead-out" restriction="v &lt; 2000" type="extended_duration_audio"/>
        <component check="true" label="Mute audio detected" name="MuteTrackFound"/>
      </item>
      <item check="false" index="0" label="Test Tone" level="3" multiple="true" name="Test Tone" severity="Serious"/>
      <item check="false" index="0" label="Level Mismatch" level="3" log="false" name="Level Mismatch" severity="Serious"/>
      <item check="false" index="0" label="DialNorm-Loudness Mismatch" level="3" log="false" multiple="true" name="DialNorm-Loudness Mismatch" severity="Serious"/>
      <item check="true" index="0" label="Clipping" level="3" log="true" multiple="true" name="Audio Clipping" severity="Serious">
        <component check="true" label="Audio Clipping persists" name="Minimum Duration" restriction="v &gt; 50" type="extended_duration_audio"/>
      </item>
      <item check="false" index="0" label="Language" level="3" log="false" name="AudioLanguage" severity="Serious"/>
      <item check="false" index="0" label="Misplaced Channels" level="3" log="false" name="Misplaced Channels" severity="Serious"/>
      <item check="false" index="0" label="Background Noise" level="3" log="true" multiple="true" name="Background Noise" severity="Serious"/>
      <item check="false" index="0" label="Transient Noise" level="3" log="false" multiple="true" name="Transient Noise" severity="Serious"/>
      <item index="0" label="Loudness" level="3" multiple="true" name="LoudnessEx" variants="CALM">
        <variant label="Loudness(CALM)" name="CALM" severity="Serious">
          <component check="false" label="DialNorm-Loudness Mismatch" log="true" name="DialNorm-Loudness Mismatch" restriction="" type="double" unit="LU"/>
          <component check="true" label="Program Loudness" log="true" name="Program Loudness" restriction="( v &lt; -26 ) or ( v &gt; -22 )" type="double" unit="LKFS"/>
          <component check="true" label="True Peak Level" log="true" name="True Peak Level" restriction="v &gt; -2" type="double" unit="dBTP"/>
        </variant>
      </item>
      <item index="0" label="Level" level="3" name="AudioLevel" variants="AverageLevel,MaximumLevel">
        <variant check="true" label="Average Level" log="true" name="AverageLevel" severity="Serious">
          <component label="Average Level" name="AverageLevel" restriction="v &gt; -9" type="double" unit="dBFS"/>
          <component enum="ChannelSelection_Centre" label="Channels" name="AvgChannels" restriction="Left" rule="==" type="enumeration"/>
          <component label="Interval" name="AvgLevelDuration" restriction="v == 1000" type="extended_duration_audio"/>
        </variant>
        <variant check="true" label="Maximum Level" log="true" name="MaximumLevel" severity="Serious">
          <component enum="ChannelSelection_Centre" label="Channels" name="MaxChannels" restriction="All" rule="==" type="enumeration"/>
          <component label="Maximum Level persists" name="MaxLevelDuration" restriction="v &gt; 200" type="extended_duration_audio"/>
          <component label="Maximum Level" name="MaximumLevel" restriction="v == -2" type="double" unit="dBFS"/>
        </variant>
      </item>
      <item check="false" index="0" label="Wow and Flutter" level="3" log="false" multiple="true" name="Wow and Flutter" severity="Serious"/>
      <item check="false" index="0" label="Jitter Noise" level="3" log="false" multiple="true" name="Jitter Noise" severity="Serious"/>
      <item check="false" index="0" label="High Frequency Noise" level="3" log="false" multiple="true" name="High Frequency Noise" severity="Serious"/>
      <item check="false" index="0" label="Stereo Pair Detection" level="3" log="false" name="Stereo Pair Detection" severity="Serious"/>
      <item check="false" index="0" label="Overmodulation" level="3" log="false" multiple="true" name="Overmodulation" severity="Serious"/>
      <item check="false" index="0" label="PPM Meter" level="3" log="false" name="PPM Meter" severity="Serious"/>
      <item check="false" index="0" label="Phase Mismatch" level="3" log="false" name="Phase Mismatch" severity="Serious"/>
      <item check="false" index="0" label="Dropout" level="3" log="false" name="Audio Dropout" severity="Serious"/>
      <item check="false" index="0" label="Click" level="3" log="false" name="Audio Click" severity="Serious"/>
      <item check="false" index="0" label="Pop" level="3" log="false" name="Audio Pop" severity="Serious"/>
      <item index="0" label="Colored Noise" level="3" name="Colored Noise" severity="Serious">
        <component check="false" label="Pink Noise persists" log="false" name="Pink Noise" restriction="" type="extended_duration_audio"/>
        <component check="false" label="White Noise persists" log="false" name="White Noise" restriction="" type="extended_duration_audio"/>
      </item>
      <item check="false" index="0" label="Crackle" level="3" log="false" name="Audio Crackle" severity="Serious"/>
      <item index="0" label="Nielsen Watermark" level="3" name="Nielsen WaterMarks" severity="Serious">
        <component check="false" complex_value_type="PIDs" label="SIDs" log="false" name="Allowed SIDs" restriction="" rule="!=" type="complex" value_format="json"/>
        <component check="false" label="Discontinuity" name="Discontinuity Interval" restriction="" type="integer" unit="seconds"/>
        <component enum="WatermarkModeWithNone" label="Ignore" name="Ignore" restriction="None" rule="==" type="enumeration"/>
        <component check="false" enum="WatermarkMode" label="Nielsen Watermark type" log="false" name="Nielsen WaterMarks" restriction="" rule="!=" type="enumeration"/>
        <component check="false" enum="OnlyPresenceEnum" label="Nielsen Watermark" log="false" name="PresenceCheck" restriction="" rule="!=" type="enumeration"/>
      </item>
      <item index="0" label="Cinavia Watermark" level="3" name="Cinavia Watermarks" severity="Serious">
        <component check="false" enum="OnlyPresenceEnum" label="Cinavia Watermark" log="false" name="Cinavia Watermarks" restriction="" rule="!=" type="enumeration"/>
        <component check="false" enum="CinaviaWatermarkType" label="Cinavia Watermark type" log="false" name="Watermark Type" restriction="" rule="!=" type="enumeration"/>
      </item>
      <item check="false" index="0" label="EAS Message" level="3" log="false" name="EAS Message" severity="Serious"/>
    </section>
    <section category="ContainerEncoding" label="Container" name="Common" summary="Container Features">
      <description>
        
        
        
        
        Container Features
      
      
      
      
      </description>
      <item check="false" index="0" label="Bitrate" level="1" log="false" name="Bitrate" severity="Serious"/>
      <item check="false" index="0" label="PID Order" level="1" log="false" name="PIDOrder" severity="Serious"/>
      <item check="false" index="0" label="Content Layout" level="3" log="false" name="ContentLayout" severity="Serious"/>
      <item index="0" label="Slates" level="3" log="false" name="Slates"/>
      <item check="false" index="0" label="File Size" level="1" log="false" name="FileSize" severity="Serious"/>
      <item check="false" index="0" label="MD5" level="1" log="true" name="MD5" severity="Serious"/>
      <item check="true" index="0" label="Video Tracks Count" level="1" log="false" name="VideoTracks" severity="Serious">
        <component check="true" label="Video Tracks Count" name="VideoTracks" restriction="v != 1" type="integer"/>
      </item>
      <item check="false" index="0" label="Audio Tracks Count" level="1" log="true" name="AudioTracks" severity="Serious"/>
      <item check="false" index="0" label="Mismatch in Audio and Video Duration" level="1" log="true" name="Audio Video Duration Mismatch" severity="Serious"/>
      <item check="false" index="0" label="Audio and Video PIDs" level="1" name="Allowable PIDs" severity="Serious">
        <component check="false" complex_value_type="PIDs" label="Audio PIDs" log="true" name="Audio PIDs" restriction="" rule="!=" type="complex" value_format="json"/>
        <component check="false" complex_value_type="PIDs" label="Dolby E PIDs" log="false" name="DolbyE PIDs" restriction="" rule="!=" type="complex" value_format="json"/>
        <component check="false" complex_value_type="PIDs" label="Video PIDs" log="true" name="Video PIDs" restriction="" rule="!=" type="complex" value_format="json"/>
      </item>
      <item check="false" index="0" label="Loudness Mismatch in Audio Tracks" level="3" log="false" name="LoudnessMismatchInTracks" severity="Serious"/>
      <item check="false" index="0" label="DID SDID" level="1" log="false" name="DIDSDID" severity="Serious"/>
      <item check="false" index="0" label="Compare System and Elementary metadata" level="1" name="Compare System and Elementary metadata" severity="Serious"/>
      <item check="false" index="0" label="Closed Captions" level="1" log="true" name="ClosedCaptions" severity="Serious"/>
      <item check="false" index="0" label="Location of Closed Captions" level="1" log="true" name="CCLocation" severity="Warning"/>
      <item check="false" index="0" label="Track Duration Mismatch" level="1" name="TrackDurationMismatch" severity="Serious"/>
      <item check="false" index="0" label="Track Sub-segment Count Mismatch" level="1" name="TrackSubsegmentCountMismatch" severity="Serious"/>
      <item index="0" label="Video Metadata Mismatch" level="1" name="VideoMetadataMismatch" severity="Serious">
        <component check="false" label="Mismatch in Average Bitrate" name="AverageBitrate" restriction="" type="double" unit="Kbps"/>
        <component check="false" label="Mismatch in Display Aspect Ratio detected" name="DisplayAspectRatio"/>
        <component check="false" label="Mismatch in Duration" name="Duration" restriction="" type="duration"/>
        <component check="false" label="Mismatch in Frame Rate detected" name="FrameRate"/>
        <component check="false" label="Mismatch in GOP Structure across tracks detected" name="GOPStructure"/>
        <component check="false" label="Mismatch in Picture Scanning Type detected" name="PictureScanningType"/>
        <component check="false" label="Mismatch in Pixel Aspect Ratio detected" name="PixelAspectRatio"/>
        <component check="false" label="Mismatch in Stored Height detected" name="StoredHeight"/>
        <component check="false" label="Mismatch in Stored Width detected" name="StoredWidth"/>
      </item>
      <item index="0" label="Audio Metadata Mismatch" level="1" name="AudioMetadataMismatch" severity="Serious">
        <component check="false" label="Mismatch in Audio Channels detected" name="AudioChannels"/>
        <component check="false" label="Mismatch in Average Bitrate" name="AverageBitrate" restriction="" type="double" unit="Kbps"/>
        <component check="false" label="Mismatch in Duration" name="Duration" restriction="" type="extended_duration"/>
        <component check="false" label="Mismatch in Sampling Frequency detected" name="SamplingFrequency"/>
      </item>
      <item check="false" index="0" label="Synchronization" level="1" name="Synchronization" severity="Serious"/>
      <item check="false" index="0" label="Loudness Range" level="3" log="false" name="LoudnessRangeMismatchInTracks" severity="Serious"/>
    </section>
    <section category="BWFAudio" label="BWF Audio" name="Common" summary="BWF Audio Features">
      <description>
        BWF Audio Features
      </description>
      <item check="false" index="0" label="BWF Version" level="1" log="true" name="BWF Version" severity="Serious"/>
      <item check="false" index="0" label="Creation Time" level="1" log="true" name="Creation Time" severity="Serious"/>
      <item check="false" index="0" label="Start Time Code" level="1" log="true" name="Start Time Code" severity="Serious"/>
      <item index="0" label="UMID" level="1" log="true" name="UMID"/>
      <item check="false" index="0" label="Chunks" level="1" log="true" name="ChunkPresence" severity="Serious"/>
    </section>
    <section category="Subtitle" label="Subtitle" name="Common" summary="Subtitle Features">
      <description>
        
        
        
        Subtitle Features
      
      
      
      </description>
      <item check="false" index="0" label="Start TimeCode" level="1" log="true" name="StartTimeCode" severity="Serious"/>
      <item check="false" index="0" label="Duration" level="1" log="true" name="Duration" severity="Serious"/>
      <item check="false" index="0" label="Estimated Language" level="1" log="false" name="EstimatedLanguage" severity=""/>
      <item check="false" index="0" label="Encoded Language" level="1" log="true" name="EncodedLanguage" severity="Serious"/>
      <item check="false" index="0" label="Validity" level="1" log="true" name="Validity" severity="Serious"/>
      <item check="false" index="0" label="Profane Words" level="1" log="false" name="ProfaneWords" severity="Serious">
        <component check="false" enum="PresentTypes" label="Profane Words" name="ProfaneWords" restriction="" rule="==" type="enumeration"/>
        <component label="Select Profane Words Dictionary" name="ProfaneWordsDictionary" restriction="All" type="ProfaneWordGroup"/>
      </item>
      <item check="false" index="0" label="Dropout" level="1" name="Dropout" severity="Serious"/>
    </section>
    <section category="MXF" label="MXF" name="Common" summary="MXF Features">
      <description>
        
        
        
        
        MXF Features
      
      
      
      
      </description>
      <item check="true" index="0" label="Operational Pattern" level="1" log="true" name="Operational Pattern" severity="Serious">
        <component check="true" enum="OperationalPattern" name="Operational Pattern" restriction="OP1a" rule="!=" type="enumeration"/>
      </item>
      <item check="false" index="0" label="Modification Date" level="1" log="true" name="Modification Date" severity="Serious"/>
      <item check="false" index="0" label="Product Name" level="1" log="true" name="Product Name" severity="Serious"/>
      <item check="false" index="0" label="Product Version" level="1" log="true" name="Product Version" severity="Serious"/>
      <item check="false" index="0" label="Company Name" level="1" log="true" name="Company Name" severity="Serious"/>
      <item check="false" index="0" label="Random Index Pack" level="1" log="true" name="Random Index Pack" severity="Serious"/>
      <item check="false" index="0" label="RunIn" level="1" log="true" name="RunIn" severity="Serious"/>
      <item check="false" index="0" label="Body Partition Length" level="1" log="true" name="Body Partition Length" severity="Serious"/>
      <item check="false" index="0" label="Body Partition Duration" level="1" log="true" name="Body Partition Duration" severity="Serious"/>
      <item check="false" index="0" label="KAG Size" level="1" log="true" name="KAG Size" severity="Serious"/>
      <item check="false" index="0" label="Essence Wrapping Type" level="1" log="true" name="Essence Wrapping Type" severity="Serious"/>
      <item check="false" index="0" label="Audio Track Layout" level="1" log="true" name="Audio Track Layout" severity="Serious"/>
      <item check="false" index="0" label="Essence Track Origin (Source Package)" level="1" log="true" name="Essence Track Origin (Source Package)" severity="Serious"/>
      <item check="false" index="0" label="Body Partition Count" level="1" log="true" name="Body Partition Count" severity="Serious"/>
      <item check="false" index="0" label="Streamable File" level="1" log="true" name="Streamable File" severity="Serious"/>
      <item check="false" index="0" label="Dark Metadata" level="1" log="true" name="Dark Metadata" severity="Serious"/>
      <item check="false" index="0" label="Descriptive Metadata" level="1" log="true" name="Descriptive Metadata" severity="Serious"/>
      <item check="false" index="0" label="KLV Fill Items" level="1" log="true" name="KLV Fill Items" severity="Serious"/>
      <item index="0" label="Index Table" level="1" name="Index Table" severity="Serious">
        <component check="false" label="Index Table Inconsistency detected " log="false" name="Consistency"/>
        <component check="false" enum="DetectionMode" label="Index Table" log="true" name="Index Table" restriction="" rule="!=" type="enumeration"/>
      </item>
      <item check="true" index="0" label="TimeCode Track (Source Package)" level="1" log="true" multiple="true" name="TimeCode Track" severity="Warning">
        <component check="false" label="Drop Frame Flag" name="Drop Frame Flag" type="enumeration"/>
        <component check="false" label="Duration" name="Duration" type="duration"/>
        <component check="false" label="Origin" name="Origin" type="integer"/>
        <component check="false" label="Rounded Timecode Base" name="Rounded Timecode Base" type="integer"/>
        <component check="true" label="Start TimeCode" name="Start TimeCode" restriction="v != 3599933" type="duration"/>
        <component check="false" label="TimeCode Discontinuity" name="TimeCode Discontinuity" type="enumeration"/>
        <component check="false" label="TimeCode Track" name="TimeCode Track" type="enumeration"/>
      </item>
      <item check="false" index="0" label="TimeCode Track (Material Package)" level="1" log="true" multiple="true" name="TimeCode Track(Material Package)" severity="Warning"/>
      <item index="0" label="Material Package UMID" level="1" log="false" name="Material Package UMID"/>
      <item index="0" label="Video Track Properties" level="1" name="Video Track Properties" severity="Serious">
        <component check="false" enum="ActiveFormatTypes" label="Active Format Descriptor" log="true" name="Active Format Descriptor" restriction="" rule="!=" type="enumeration"/>
        <component check="false" label="Bitrate" log="false" name="Bitrate" restriction="" type="double" unit="Mbps"/>
        <component check="false" label="Black Reference Level" log="false" name="Black Reference Level" restriction="" type="integer"/>
        <component check="false" enum="ChromaFormat" label="Chroma Format" log="true" name="Chroma Format" restriction="" rule="!=" type="enumeration"/>
        <component check="false" label="Display Aspect Ratio Height" log="false" name="Display Aspect Ratio Height" restriction="" type="integer"/>
        <component check="false" label="Display Aspect Ratio Width" log="false" name="Display Aspect Ratio Width" restriction="" type="integer"/>
        <component check="false" label="Display Height" log="false" name="Display Height" restriction="" type="integer" unit="Pixels"/>
        <component check="false" label="Display Width" log="false" name="Display Width" restriction="" type="integer" unit="Pixels"/>
        <component check="false" complex_value_type="VideoResolution" label="Display WxH" log="false" name="Display WxH" restriction="" rule="!=" type="complex" value_format="json"/>
        <component check="false" label="Edit Rate Denominator" log="false" name="Edit Rate Denominator" restriction="" type="integer"/>
        <component check="false" label="Edit Rate Numerator" log="false" name="Edit Rate Numerator" restriction="" type="integer"/>
        <component check="false" label="Essence Container Type" log="false" name="Essence Container Type" type="enumeration"/>
        <component check="false" enum="FieldDominance" label="Field Dominance" log="false" name="Field Dominance" restriction="" rule="!=" type="enumeration"/>
        <component check="false" enum="FrameLayout" label="Frame Layout" log="false" name="Frame Layout" restriction="" rule="!=" type="enumeration"/>
        <component check="false" label="Frame Rate" log="false" name="Frame Rate" restriction="" type="double" unit="Fps"/>
        <component check="false" enum="SampledTopness" label="Sampled Topness" log="false" name="Sampled Topness" restriction="" rule="!=" type="enumeration"/>
        <component check="false" label="Stored Height" log="false" name="Stored Height" restriction="" type="integer" unit="Pixels"/>
        <component check="false" label="Stored Width" log="false" name="Stored Width" restriction="" type="integer" unit="Pixels"/>
        <component check="false" complex_value_type="VideoResolution" label="Stored WxH" log="false" name="Stored WxH" restriction="" rule="!=" type="complex" value_format="json"/>
        <component check="false" enum="TransferCharactersitic" label="Transfer Characteristic" log="false" name="Transfer Characteristic" restriction="" rule="!=" type="enumeration"/>
        <component check="false" label="Video Essence Type" log="false" name="Video Essence Type" type="enumeration"/>
        <component check="false" label="Video Line Map 0" log="false" name="Video Line Map 0" restriction="" type="integer"/>
        <component check="false" label="Video Line Map 1" log="false" name="Video Line Map 1" restriction="" type="integer"/>
        <component check="false" label="White Reference Level" log="false" name="White Reference Level" restriction="" type="integer"/>
      </item>
      <item index="0" label="Audio Track Properties" level="1" name="Audio Track Properties" severity="Serious">
        <component check="false" label="Channel Count" log="true" name="Channel Count" restriction="" type="integer"/>
        <component check="false" label="Quantization Bits" log="true" name="Quantization Bits" restriction="" type="integer"/>
        <component check="false" label="Sample Rate" log="true" name="Sample Rate" restriction="" type="double"/>
      </item>
      <item index="0" label="System Item" level="1" multiple="true" name="System Item" severity="Serious">
        <component check="false" label="Mismatch in LTC and VITC timecode" name="Check LTC VITC mismatch"/>
        <component check="false" complex_value_type="TimeCodeFrame" label="LTC TimeCode" log="false" name="LTC TimeCode" restriction="" rule="!=" type="complex" value_format="json"/>
        <component check="false" complex_value_type="TimeCodeFrame" label="Start TimeCode" log="true" name="Start TimeCode" restriction="" rule="!=" type="complex" value_format="json"/>
        <component check="false" complex_value_type="TimeCodeFrame" label="VITC TimeCode" log="false" name="VITC TimeCode" restriction="" rule="!=" type="complex" value_format="json"/>
      </item>
      <item check="false" index="0" label="System Item Timecode Discontinuity" level="1" name="System Item Timecode Discontinuity" severity="Serious"/>
      <item index="0" label="Compare Start Timecodes" level="1" name="CompareStartTimeCodes" severity="">
        <component check="false" label="Mismatch in GOP Header and Source Package Start Timecodes" name="Mismatch in GOP Header and Source Package Start Timecodes"/>
        <component check="false" label="Mismatch in Material Package and Source Package Start Timecodes" name="Mismatch in Material Package and Source Package Start Timecodes"/>
        <component check="false" label="Mismatch in System Item and Material Package Start Timecodes" name="Mismatch in System Item and Material Package Start Timecodes"/>
        <component check="false" label="Mismatch in System Item and Source Package Start Timecodes" name="Mismatch in System Item and Source Package Start Timecodes"/>
      </item>
      <item index="0" label="Partition Status" level="1" name="Partition Status" severity="Serious">
        <component check="false" enum="PartitionStatus" label="Footer Partition" log="true" name="Footer Partition" restriction="" rule="!=" type="enumeration"/>
        <component check="false" enum="PartitionStatus" label="Header Partition" log="true" name="Header Partition" restriction="" rule="!=" type="enumeration"/>
      </item>
    </section>
    <section category="MPEG2Video" label="MPEG-2 Video" name="Common" summary="MPEG-2 Video Features">
      <description>
        
        
        
        
        MPEG-2 Video Features
      
      
      
      
      </description>
      <item check="true" index="0" label="Profile" level="1" log="true" name="Profile" severity="Serious">
        <component check="true" enum="MPEG2VideoProfiles" name="Profile" restriction="4:2:2" rule="!=" type="enumeration"/>
      </item>
      <item check="true" index="0" label="Level" level="1" log="true" name="Level" severity="Serious">
        <component check="true" enum="MPEG2VideoLevels" name="Level" restriction="High" rule="!=" type="enumeration"/>
      </item>
      <item check="false" index="0" label="bit_rate_extension" level="1" log="false" name="bit_rate_extension" severity="Serious"/>
      <item check="false" index="0" label="temporal_reference" level="1" name="temporal_reference" severity="Serious"/>
      <item check="false" index="0" label="intra_dc_precision" level="1" name="intra_dc_precision" severity="Serious"/>
      <item check="false" index="0" label="vbv_delay" level="1" name="vbv_delay" severity="Serious"/>
      <item check="false" index="0" label="OP47 Data" level="1" log="false" name="OP47 Data" severity="Serious"/>
      <item check="true" index="0" label="Encoded bitrate" level="1" log="true" name="Encoded bitrate" severity="Serious">
        <component check="true" label="Encoded Bitrate" name="Encoded bitrate" restriction="v != 50" type="double" unit="Mbps"/>
      </item>
      <item check="false" index="0" label="Frame Size" level="3" name="FrameSize" severity="Serious"/>
      <item check="false" index="0" label="MB Count per Slice" level="2" name="MB Count per Slice" severity="Serious"/>
      <item check="false" index="0" label="bit_rate_value" level="1" log="false" name="bit_rate_value" severity="Serious"/>
      <item check="false" index="0" label="SeqHdr and SeqExtn" level="1" name="SeqHdr and SeqExtn in every frame" severity="Serious"/>
      <item check="false" index="0" label="alternate_scan" level="1" name="alternate_scan" severity="Serious"/>
      <item check="false" index="0" label="frame_pred_frame_dct" level="1" name="frame_pred_frame_dct" severity="Serious"/>
      <item check="false" index="0" label="top_field_first" level="1" log="true" name="top_field_first" severity="Serious"/>
      <item check="false" index="0" label="repeat_first_field" level="1" name="repeat_first_field" severity="Serious"/>
      <item check="false" index="0" label="progressive_frame" level="1" name="progressive_frame" severity="Serious"/>
      <item check="false" index="0" label="progressive_sequence" level="1" log="true" name="progressive_sequence" severity="Serious"/>
      <item check="false" index="0" label="picture_structure" level="1" log="false" name="picture_structure" severity="Serious"/>
      <item check="false" index="0" label="q_scale_type" level="1" name="q_scale_type" severity="Serious"/>
      <item check="false" index="0" label="intra_vlc_format" level="1" name="intra_vlc_format" severity="Serious"/>
      <item check="false" index="0" label="GOP Status" level="1" log="false" name="GOP Status" severity="Serious"/>
      <item check="false" index="0" label="Picture Coding Type" level="1" log="false" name="Picture Coding Type" severity="Serious"/>
      <item index="0" label="GOP Header" level="3" name="gop_header" severity="Serious">
        <component check="false" enum="TrueOrFalse" label="Drop Frame Flag" log="false" name="drop_frame_flag" restriction="" rule="!=" type="enumeration"/>
        <component label="GOP Start Timecode" log="false" name="start_timecode"/>
      </item>
      <item check="false" index="0" label="Caption Data" level="3" log="false" name="Caption Data" severity="Serious"/>
      <item check="false" index="0" label="VITC PAL/NTSC" level="3" log="false" name="VITC PAL" severity="Serious"/>
      <item check="false" index="0" label="WSS PAL" level="3" log="false" name="Line 23 WSS PAL" severity="Serious"/>
      <item check="false" index="0" label="Subtitles in Teletext PAL" level="3" log="false" name="Subtitles in Teletext PAL" severity="Serious"/>
      <item index="0" label="SMPTE328M Timecode" level="3" name="SMPTE328M Timecode" severity="Serious">
        <component check="false" label="Start Timecode" log="false" name="SMPTE328M Start Timecode" restriction="" type="duration"/>
        <component check="false" label="SMPTE328M Timecode Discontinuity" name="SMPTE328M Timecode Discontinuity" restriction="" type="integer" unit="Frames"/>
      </item>
    </section>
  </sections>
</testplan>
