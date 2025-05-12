## Problem Description

Little Timmy has been experimenting with home automation! He has some ESP32-C6 Zigbee devices and put an important flag in the firmware. He has since lost the flag and is having a hard time finding it in the source, can you get it for him?

## Problem Solution

1. Open Ghidra and locate the Entry Point

    * No traditional main() exists; this is an embedded FreeRTOS firmware
    * So the main logic starts in app_main()
    *Inside app_main, find a build_flag_task()

### build_flag_task()

This function allocates a buffer and builds the flag step by step:
```c
void build_flag_task(void)

{
  char cVar1;
  char cVar2;
  char cVar3;
  char cVar4;
  char cVar5;
  char cVar6;
  char cVar7;
  char cVar8;
  char *flag;
  BaseType_t BVar9;
  int lastpart;
  char *flag_str;
  char uVar1;
  
  gp = 0x4080fb94;
  esp_log_timestamp();
  esp_log((esp_log_config_t)0x3,s_ESP_OTA_CLIENT_42063488,
          s_I_(%lu)_%s:_Waiting_for_Zigbee_n_42063708);
  xEventGroupWaitBits(zigbee_event_group_flag,1,1,1,0xffffffff);
  flag = (char *)malloc(0x26);
  if (flag == (char *)0x0) {
    puts(s_Memory_allocation_failed_42063740);
    vTaskDelete((TaskHandle_t)0x0);
  }
  BVar9 = xQueueSemaphoreTake(xStringMutex,0xffffffff);
  if (BVar9 != 0) {
    printf(s_Task_2_received:_%s_4206375c,sharedString);
    xQueueGenericSend(xStringMutex,(void *)0x0,0,0);
    cVar3 = DAT_42063778;
    cVar2 = DAT_42063777;
    cVar1 = DAT_42063776;
    uVar1 = DAT_42063775;
    *flag = DAT_42063774;
    flag[1] = uVar1;
    flag[2] = cVar1;
    flag[3] = cVar2;
    flag[4] = cVar3;
    strcat(flag,sharedString);
    lastpart = strlen(flag);
    cVar8 = s__on_the__4206377c[8];
    cVar7 = s__on_the__4206377c[7];
    cVar6 = s__on_the__4206377c[6];
    cVar5 = s__on_the__4206377c[5];
    cVar4 = s__on_the__4206377c[4];
    cVar3 = s__on_the__4206377c[3];
    cVar2 = s__on_the__4206377c[2];
    cVar1 = s__on_the__4206377c[1];
    flag_str = flag + lastpart;
    *flag_str = s__on_the__4206377c[0];
    flag_str[1] = cVar1;
    flag_str[2] = cVar2;
    flag_str[3] = cVar3;
    flag_str[4] = cVar4;
    flag_str[5] = cVar5;
    flag_str[6] = cVar6;
    flag_str[7] = cVar7;
    flag_str[8] = cVar8;
    lastpart = strlen(flag);
    cVar7 = DAT_4206378f;
    cVar6 = DAT_4206378e;
    cVar5 = DAT_4206378d;
    cVar4 = DAT_4206378c;
    cVar3 = DAT_4206378b;
    cVar2 = DAT_4206378a;
    cVar1 = DAT_42063789;
    flag_str = flag + lastpart;
    *flag_str = DAT_42063788;
    flag_str[1] = cVar1;
    flag_str[2] = cVar2;
    flag_str[3] = cVar3;
    flag_str[4] = cVar4;
    flag_str[5] = cVar5;
    flag_str[6] = cVar6;
    flag_str[7] = cVar7;
    lastpart = strlen(flag);
    flag[lastpart] = '}';
    (flag + lastpart)[1] = '\0';
  }
  esp_log_timestamp();
  esp_log((esp_log_config_t)0x3,s_ESP_OTA_CLIENT_42063488,s_I_(%lu)_%s:_Flag:_%s_42063790);
  free(flag);
  vTaskDelete((TaskHandle_t)0x0);
  return;
}
```


First, this function allocates a buffer and builds the flag in chunks.

```c
uVar4 = DAT_42063778;
    uVar3 = DAT_42063777;
    uVar2 = DAT_42063776;
    uVar1 = DAT_42063775;
    *__ptr = DAT_42063774;
    __ptr[1] = uVar1;
    __ptr[2] = uVar2;
    __ptr[3] = uVar3;
    __ptr[4] = uVar4;
```
This function is equal to:

```c
__ptr = malloc(0x26);  // allocate memory
*__ptr = 'd';
__ptr[1] = 'a';
__ptr[2] = 'm';
__ptr[3] = '{';
__ptr[4] = '\0'; // string terminator → this means only "dam{" is kept at first
```
Next, we see:

```c
strcat(__ptr, sharedString);
```

This is critical: the real flag content is stored in sharedString, which is written elsewhere.

Then:
```c
cVar12 = s__on_the__4206377c[8];
    cVar11 = s__on_the__4206377c[7];
    cVar10 = s__on_the__4206377c[6];
    cVar9 = s__on_the__4206377c[5];
    cVar8 = s__on_the__4206377c[4];
    cVar7 = s__on_the__4206377c[3];
    cVar6 = s__on_the__4206377c[2];
    cVar5 = s__on_the__4206377c[1];
    pcVar18 = __ptr + iVar17;
    *pcVar18 = s__on_the__4206377c[0];
    pcVar18[1] = cVar5;
    pcVar18[2] = cVar6;
    pcVar18[3] = cVar7;
    pcVar18[4] = cVar8;
    pcVar18[5] = cVar9;
    pcVar18[6] = cVar10;
    pcVar18[7] = cVar11;
    pcVar18[8] = cVar12;
```

This code is also translated as:

```c
strcat(__ptr, "_on_the_");
strcat(__ptr, "esp32c6v");
```

And finally:

```c
__ptr[iVar17] = '}';  // appends the final brace
```

Following these instructions, we could find a stucture of the flag.

```c
flag: dam{<sharedString>_on_the_esp32c6v}
```

So we need to find sharedString to put inside the flag.

## esp_zb_app_signal_handler

```c
void esp_zb_app_signal_handler(undefined4 *param_1)

{
  uint uVar1;
  int iVar2;
  BaseType_t BVar3;
  undefined1 auStack_38 [8];
  
  iVar2 = param_1[1];
  uVar1 = *(uint *)*param_1;
  if (uVar1 < 7) {
    if (4 < uVar1) {
      if (iVar2 != 0) {
        esp_log_timestamp();
        esp_zb_zdo_signal_to_string(uVar1);
        esp_err_to_name(iVar2);
        esp_log((esp_log_config_t)0x2,s_ESP_OTA_CLIENT_42063488,
                s_W_(%lu)_%s:_%s_failed_with_statu_42063f78);
        esp_zb_scheduler_alarm(bdb_start_top_level_commissioning_cb,0,1000);
        return;
      }
      esp_log_timestamp();
      deferred_driver_init();
      esp_log((esp_log_config_t)0x3,s_ESP_OTA_CLIENT_42063488,
              s_I_(%lu)_%s:_Deferred_driver_init_42063ecc);
      esp_log_timestamp();
      esp_zb_bdb_is_factory_new();
      esp_log((esp_log_config_t)0x3,s_ESP_OTA_CLIENT_42063488,
              s_I_(%lu)_%s:_Device_started_up_in_42063efc);
      iVar2 = esp_zb_bdb_is_factory_new();
      if (iVar2 != 0) {
        esp_log_timestamp();
        esp_log((esp_log_config_t)0x3,s_ESP_OTA_CLIENT_42063488,
                s_I_(%lu)_%s:_Start_network_steeri_42063f34);
        esp_zb_bdb_start_top_level_commissioning(2);
        return;
      }
      esp_log_timestamp();
      esp_log((esp_log_config_t)0x3,s_ESP_OTA_CLIENT_42063488,s_I_(%lu)_%s:_Device_rebooted_42063f58
             );
      return;
    }
    if (uVar1 == 1) {
      esp_log_timestamp();
      esp_log((esp_log_config_t)0x3,s_ESP_OTA_CLIENT_42063488,
              s_I_(%lu)_%s:_Initialize_Zigbee_st_42063ea4);
      esp_zb_bdb_start_top_level_commissioning(0);
      return;
    }
  }
  else if (uVar1 == 10) {
    if (iVar2 != 0) {
      esp_log_timestamp();
      esp_err_to_name(iVar2);
      esp_log((esp_log_config_t)0x3,s_ESP_OTA_CLIENT_42063488,
              s_I_(%lu)_%s:_Network_steering_was_4206405c);
      esp_zb_scheduler_alarm(bdb_start_top_level_commissioning_cb,2,5000);
      return;
    }
    esp_zb_get_extended_pan_id(auStack_38);
    xEventGroupSetBits(zigbee_event_group_flag,1);
    esp_log_timestamp();
    esp_zb_get_pan_id();
    esp_zb_get_current_channel();
    esp_zb_get_short_address();
    esp_log((esp_log_config_t)0x3,s_ESP_OTA_CLIENT_42063488,
            s_I_(%lu)_%s:_Joined_network_succe_42063fac);
    BVar3 = xQueueSemaphoreTake(xStringMutex,0xffffffff);
    if (BVar3 == 0) {
      return;
    }
    sharedString[0] = (char)DAT_42064048;
    sharedString[1] = DAT_42064048._1_1_;
    sharedString[2] = DAT_42064048._2_1_;
    sharedString[3] = DAT_42064048._3_1_;
    sharedString[4] = (char)DAT_4206404c;
    sharedString[5] = DAT_4206404c._1_1_;
    sharedString[6] = DAT_4206404c._2_1_;
    sharedString[7] = DAT_4206404c._3_1_;
    sharedString[8] = (char)DAT_42064050;
    sharedString[9] = DAT_42064050._1_1_;
    sharedString[10] = DAT_42064050._2_1_;
    sharedString[0xb] = DAT_42064050._3_1_;
    sharedString[0xc] = (char)DAT_42064054;
    sharedString[0xd] = DAT_42064054._1_1_;
    sharedString[0xe] = DAT_42064054._2_1_;
    sharedString[0xf] = DAT_42064054._3_1_;
    sharedString[0x10] = DAT_42064058;
    xQueueGenericSend(xStringMutex,(void *)0x0,0,0);
    return;
  }
  esp_log_timestamp();
  esp_zb_zdo_signal_to_string(uVar1);
  esp_err_to_name(iVar2);
  esp_log((esp_log_config_t)0x3,s_ESP_OTA_CLIENT_42063488,
          s_I_(%lu)_%s:_ZDO_signal:_%s_(0x%x_4206409c);
  return;
}
```

Each memory block was checked in Ghidra using its hex values, and converted to ASCII:

```c
0x42064048: 46 72 33 33 → 'Fr33'
0x4206404c: 52 37 30 35 → 'R705'
0x42064050: 5f 31 35 5f → '_15_'
0x42064054: 43 30 30 31 → 'C001'
```

## Flag

```c
dam{Fr33R705_15_C001_on_the_esp32c6v}
```