TYPE
    SdcHwCfg_typ : STRUCT
        EncIf1_Typ          :UINT;
        EncIf2_Typ          :UINT;
        DrvIf_Typ           :UINT;
        TrigIf1_Typ         :UINT;
        TrigIf2_Typ         :UINT;
        DiDoIf_Typ          :UINT;
        EncIf1_Name         :ARRAY[0..33] OF USINT;
        EncIf2_Name         :ARRAY[0..33] OF USINT;
        DrvIf_Name          :ARRAY[0..33] OF USINT;
        TrigIf1_Name        :ARRAY[0..33] OF USINT;
        TrigIf2_Name        :ARRAY[0..33] OF USINT;
        DiDoIf_Name         :ARRAY[0..33] OF USINT;
        NOT_USE             :ARRAY[0..9] OF UDINT;
    END_STRUCT;
    SdcEncIf16_typ : STRUCT
        iLifeCnt            :SINT;
        iEncOK              :BOOL;
        iActTime            :INT;
        iActPos             :INT;
        iRefPulsePos        :INT;
        iRefPulseCnt        :SINT;
        reserve             :ARRAY[0..2] OF BOOL;
    END_STRUCT;
    SdcEncIf32_typ : STRUCT
        iLifeCnt            :SINT;
        iEncOK              :BOOL;
        iActTime            :INT;
        iActPos             :DINT;
        iRefPulsePos        :DINT;
        iRefPulseCnt        :SINT;
        reserve             :ARRAY[0..2] OF BOOL;
    END_STRUCT;
    SdcDrvIf16_typ : STRUCT
        iLifeCnt            :SINT;
        iDrvOK              :BOOL;
        oSetTime            :INT;
        oSetPos             :INT;
        oBoostCurrent       :BOOL;
        oStandStillCurrent  :BOOL;
        iStatusEnable       :BOOL;
        oBrake              :BOOL;
        reserve             :ARRAY[0..1] OF BOOL;
    END_STRUCT;
    SdcDrvIf32_typ : STRUCT
        iLifeCnt            :SINT;
        iDrvOK              :BOOL;
        oSetTime            :INT;
        oSetPos             :DINT;
        oBoostCurrent       :BOOL;
        oStandStillCurrent  :BOOL;
        iStatusEnable       :BOOL;
        oBrake              :BOOL;
    END_STRUCT;
    SdcTrigIf_typ : STRUCT
        iLifeCnt            :SINT;
        iTriggerCntRise     :SINT;
        iTriggerCntFall     :SINT;
        iTriggerInput       :BOOL;
        iTriggerTimeRise    :INT;
        iTriggerTimeFall    :INT;
    END_STRUCT;
    SdcTrigIfDIGin_typ : STRUCT
        iLifeCnt            :SINT;
        iTriggerInput       :BOOL;
        reserve             :ARRAY[0..1] OF BOOL;
    END_STRUCT;
    SdcDiDoIf_typ : STRUCT
        iLifeCntDriveReady  :SINT;
        iLifeCntPosHwEnd    :SINT;
        iLifeCntNegHwEnd    :SINT;
        iLifeCntReference   :SINT;
        iLifeCntDriveEnable :SINT;
        iDriveReady         :BOOL;
        iPosHwEnd           :BOOL;
        iNegHwEnd           :BOOL;
        iReference          :BOOL;
        oDriveEnable        :BOOL;
        reserve             :ARRAY[0..1] OF BOOL;
    END_STRUCT;
END_TYPE

