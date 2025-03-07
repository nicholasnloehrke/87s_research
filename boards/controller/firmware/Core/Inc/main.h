/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2025 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32u5xx_hal.h"

#include "stm32u5xx_ll_ucpd.h"
#include "stm32u5xx_ll_bus.h"
#include "stm32u5xx_ll_cortex.h"
#include "stm32u5xx_ll_rcc.h"
#include "stm32u5xx_ll_system.h"
#include "stm32u5xx_ll_utils.h"
#include "stm32u5xx_ll_pwr.h"
#include "stm32u5xx_ll_gpio.h"
#include "stm32u5xx_ll_dma.h"

#include "stm32u5xx_ll_exti.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define EXP_PC13_Pin GPIO_PIN_13
#define EXP_PC13_GPIO_Port GPIOC
#define EXP_PC14_Pin GPIO_PIN_14
#define EXP_PC14_GPIO_Port GPIOC
#define TP_INT_Pin GPIO_PIN_15
#define TP_INT_GPIO_Port GPIOC
#define CHG_ACOK_Pin GPIO_PIN_0
#define CHG_ACOK_GPIO_Port GPIOC
#define CHG_STAT_Pin GPIO_PIN_1
#define CHG_STAT_GPIO_Port GPIOC
#define CHG_EN_Pin GPIO_PIN_2
#define CHG_EN_GPIO_Port GPIOC
#define EXP_PC3_Pin GPIO_PIN_3
#define EXP_PC3_GPIO_Port GPIOC
#define BLS_CH1_Pin GPIO_PIN_0
#define BLS_CH1_GPIO_Port GPIOA
#define BLS_CH2_Pin GPIO_PIN_1
#define BLS_CH2_GPIO_Port GPIOA
#define BLS_CH3_Pin GPIO_PIN_2
#define BLS_CH3_GPIO_Port GPIOA
#define BLS_CH4_Pin GPIO_PIN_3
#define BLS_CH4_GPIO_Port GPIOA
#define BLS_STATUS_Pin GPIO_PIN_4
#define BLS_STATUS_GPIO_Port GPIOA
#define BLS_FAULT_RESET_Pin GPIO_PIN_5
#define BLS_FAULT_RESET_GPIO_Port GPIOA
#define BLS_CH5_Pin GPIO_PIN_6
#define BLS_CH5_GPIO_Port GPIOA
#define BLS_CH6_Pin GPIO_PIN_7
#define BLS_CH6_GPIO_Port GPIOA
#define EXP_PC4_Pin GPIO_PIN_4
#define EXP_PC4_GPIO_Port GPIOC
#define EXP_PC5_Pin GPIO_PIN_5
#define EXP_PC5_GPIO_Port GPIOC
#define BLS_CH7_Pin GPIO_PIN_0
#define BLS_CH7_GPIO_Port GPIOB
#define BLS_CH8_Pin GPIO_PIN_1
#define BLS_CH8_GPIO_Port GPIOB
#define ENC1_A_Pin GPIO_PIN_2
#define ENC1_A_GPIO_Port GPIOB
#define ENC1_B_Pin GPIO_PIN_10
#define ENC1_B_GPIO_Port GPIOB
#define ENC1_BTN_Pin GPIO_PIN_12
#define ENC1_BTN_GPIO_Port GPIOB
#define ENC2_A_Pin GPIO_PIN_13
#define ENC2_A_GPIO_Port GPIOB
#define ENC2_B_Pin GPIO_PIN_14
#define ENC2_B_GPIO_Port GPIOB
#define ENC2_BTN_Pin GPIO_PIN_6
#define ENC2_BTN_GPIO_Port GPIOC
#define ENC3_A_Pin GPIO_PIN_7
#define ENC3_A_GPIO_Port GPIOC
#define ENC3_B_Pin GPIO_PIN_8
#define ENC3_B_GPIO_Port GPIOC
#define ENC3_BTN_Pin GPIO_PIN_9
#define ENC3_BTN_GPIO_Port GPIOC
#define EXP_PA8_Pin GPIO_PIN_8
#define EXP_PA8_GPIO_Port GPIOA
#define EXP_PA9_Pin GPIO_PIN_9
#define EXP_PA9_GPIO_Port GPIOA
#define EXP_PA10_Pin GPIO_PIN_10
#define EXP_PA10_GPIO_Port GPIOA
#define LCD_BL_Pin GPIO_PIN_10
#define LCD_BL_GPIO_Port GPIOC
#define LCD_RST_Pin GPIO_PIN_11
#define LCD_RST_GPIO_Port GPIOC
#define LCD_DC_Pin GPIO_PIN_12
#define LCD_DC_GPIO_Port GPIOC
#define LCD_CS_Pin GPIO_PIN_2
#define LCD_CS_GPIO_Port GPIOD
#define LCD_SCK_Pin GPIO_PIN_3
#define LCD_SCK_GPIO_Port GPIOB
#define LCD_MISO_Pin GPIO_PIN_4
#define LCD_MISO_GPIO_Port GPIOB
#define LCD_MOSI_Pin GPIO_PIN_5
#define LCD_MOSI_GPIO_Port GPIOB
#define SD_CS_Pin GPIO_PIN_6
#define SD_CS_GPIO_Port GPIOB
#define TP_RST_Pin GPIO_PIN_7
#define TP_RST_GPIO_Port GPIOB
#define BOOT0_Pin GPIO_PIN_3
#define BOOT0_GPIO_Port GPIOH
#define TP_SCL_Pin GPIO_PIN_8
#define TP_SCL_GPIO_Port GPIOB
#define TP_SDA_Pin GPIO_PIN_9
#define TP_SDA_GPIO_Port GPIOB

/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
