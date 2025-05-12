
void app_main(void)

{
  uint32_t uVar1;
  int iVar2;
  char auStack_70;
  
  gp = 0x4080fb94;
  zigbee_event_group_flag = xEventGroupCreate();
  xStringMutex = xQueueCreateMutex('\x01');
  if (xStringMutex == (QueueHandle_t)0x0) {
    uVar1 = esp_log_timestamp();
    esp_log((esp_log_config_t)0x1,s_ESP_OTA_CLIENT_42063488,
            s_E_(%lu)_%s:_Error_with_string_mu_420640cc,uVar1,s_ESP_OTA_CLIENT_42063488);
  }
  uVar1 = esp_log_timestamp();
  esp_log((esp_log_config_t)0x2,s_ESP_OTA_CLIENT_42063488,
          s_W_(%lu)_%s:_Modified_ESP_Zigbee_O_420640f4,uVar1,s_ESP_OTA_CLIENT_42063488);
  memset(&auStack_70,0,0x60);
  iVar2 = nvs_flash_init();
  if (iVar2 == 0) {
    iVar2 = esp_zb_platform_config(&auStack_70);
    if (iVar2 == 0) {
      xTaskCreatePinnedToCore
                (build_flag_task,s_build_flag_task_42064164,0x800,(void *)0x0,1,(TaskHandle_t *)0x0,
                 0x7fffffff);
      xTaskCreatePinnedToCore
                (esp_zb_task,s_Zigbee_main_42064174,0x1000,(void *)0x0,5,(TaskHandle_t *)0x0,
                 0x7fffffff);
      return;
    }
                    /* WARNING: Subroutine does not return */
    _esp_error_check_failed
              (iVar2,s_./main/esp_ota_client.c_42063b50,0x18e,__func__.9,
               s_esp_zb_platform_config(&config)_42064144);
  }
                    /* WARNING: Subroutine does not return */
  _esp_error_check_failed
            (iVar2,s_./main/esp_ota_client.c_42063b50,0x18d,__func__.9,s_nvs_flash_init()_42064130);
}


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


void esp_zb_task(void)

{
  int iVar1;
  undefined4 local_20;
  undefined4 uStack_1c;
  undefined4 uStack_18;
  undefined4 uStack_14;
  
  local_20 = DAT_4206d134;
  uStack_1c = DAT_4206d138;
  uStack_18 = DAT_4206d13c;
  uStack_14 = DAT_4206d140;
  esp_zb_init(&local_20);
  esp_zb_core_action_handler_register(zb_action_handler);
  esp_zb_set_primary_network_channel_set(0x7fff800);
  iVar1 = zb_register_ota_upgrade_client_device();
  if (iVar1 != 0) {
                    /* WARNING: Subroutine does not return */
    _esp_error_check_failed
              (iVar1,s_./main/esp_ota_client.c_42063b50,0x159,__func__.8,
               s_zb_register_ota_upgrade_client_d_42063e4c);
  }
  iVar1 = esp_zb_start(0);
  if (iVar1 == 0) {
    esp_zb_stack_main_loop();
    return;
  }
                    /* WARNING: Subroutine does not return */
  _esp_error_check_failed
            (iVar1,s_./main/esp_ota_client.c_42063b50,0x15a,__func__.8,
             s_esp_zb_start(false)_42063e74);
}