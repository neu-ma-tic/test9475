﻿using Newtonsoft.Json;
using System;
using System.IO;
using static PakReader.AssetReader;

namespace PakReader
{
    public struct FLinearColor
    {
        public float r;
        public float g;
        public float b;
        public float a;

        [JsonProperty]
        public string Hex => a == 1 || a == 0 ?
            ToHex((byte)Math.Round(r * 255), (byte)Math.Round(g * 255), (byte)Math.Round(b * 255)) :
            ToHex((byte)Math.Round(a * 255), (byte)Math.Round(r * 255), (byte)Math.Round(g * 255), (byte)Math.Round(b * 255));

        internal FLinearColor(BinaryReader reader)
        {
            r = reader.ReadSingle();
            g = reader.ReadSingle();
            b = reader.ReadSingle();
            a = reader.ReadSingle();
        }
    }
}
