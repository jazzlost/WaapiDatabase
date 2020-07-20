

################################Config############################################

# User-difined expression
formula_expression = lambda x: x-50

# User-defined properties which can be formula, please see https://www.audiokinetic.com/library/edge/?source=SDK&id=wobjects_index.html
formula_properties_dict = {
    ############################Audio Object#################################
    "Voice": "@Volume",
    "Pitch": "@Pitch",
    "Low-pass filter": "@Lowpass",
    "High-pass filter": "@Highpass",
    "Initial Delay": "@InitialDelay",
    "User-Defined Auxiliary Send Volume 0": "@UserAuxSendVolume0",
    "User-Defined Auxiliary Send Volume 1": "@UserAuxSendVolume1",
    "Game-Defined Auxiliary Sends Volume": "@GameAuxSendVolume",
    "Sound Instance Limit": "@MaxSoundPerInstance",
    "Playback Priority": "@Priority",
    "Bus Volume": "@BusVolume",

    ############################Attenuation Object #################################
    "Attenuation RadiusMax": "@RadiusMax",
    "ConeAttenuation RadiusMax": "@ConeAttenuation",

    ############################Effects Object #################################
    "WwiseGain Full Band Gain": "@FullBandGain",
    "WwiseGain LFE Gain": "@LFEGain",
    "WwiseRoomVerb Decay Time": "@DecayTime",
    "WwiseRoomVerb Dry Level": "@DryLevel",
    "WwiseRoomVerb Pre Delay": "@PreDelay",
    "WwiseTremolo Depth": "@ModDepth",

}
            