/**
 * 统一响应结果类
 * 用于规范化 API 返回格式
 */
/**
 * 响应状态码枚举
 */
export enum ResponseCode {
  SUCCESS = 200,
  BAD_REQUEST = 400,
  UNAUTHORIZED = 401,
  FORBIDDEN = 403,
  NOT_FOUND = 404,
  INTERNAL_SERVER_ERROR = 500,
}

/**
 * 统一响应结果接口
 */
export interface IResponse<T = any> {
  code: number;
  message: string;
  data?: T;
  timestamp?: number;
}

/**
 * 统一响应结果类
 */
export class Response<T = any> {
  /**
   * 响应状态码
   */
  code: number;

  /**
   * 响应消息
   */
  message: string;

  /**
   * 响应数据
   */
  data?: T;

  constructor(code: number, message: string, data?: T) {
    this.code = code;
    this.message = message;
    this.data = data;
  }

  /**
   * 成功响应
   * @param data 响应数据
   * @param message 响应消息
   * @returns Response 实例
   */
  static success<T>(data?: T, message: string = 'success'): Response<T> {
    return new Response(ResponseCode.SUCCESS, message, data);
  }

  /**
   * 失败响应
   * @param message 错误消息
   * @param code 错误码
   * @param data 额外数据
   * @returns Response 实例
   */
  static error<T>(
    message: string = '操作失败',
    code: number = ResponseCode.INTERNAL_SERVER_ERROR,
    data?: T,
  ): Response<T> {
    return new Response(code, message, data);
  }

  /**
   * 参数错误响应
   * @param message 错误消息
   * @param data 额外数据
   * @returns Response 实例
   */
  static badRequest<T>(message: string = '参数错误', data?: T): Response<T> {
    return new Response(ResponseCode.BAD_REQUEST, message, data);
  }

  /**
   * 未授权响应
   * @param message 错误消息
   * @param data 额外数据
   * @returns Response 实例
   */
  static unauthorized<T>(message: string = '未授权', data?: T): Response<T> {
    return new Response(ResponseCode.UNAUTHORIZED, message, data);
  }

  /**
   * 禁止访问响应
   * @param message 错误消息
   * @param data 额外数据
   * @returns Response 实例
   */
  static forbidden<T>(message: string = '禁止访问', data?: T): Response<T> {
    return new Response(ResponseCode.FORBIDDEN, message, data);
  }

  /**
   * 资源未找到响应
   * @param message 错误消息
   * @param data 额外数据
   * @returns Response 实例
   */
  static notFound<T>(message: string = '资源未找到', data?: T): Response<T> {
    return new Response(ResponseCode.NOT_FOUND, message, data);
  }

  /**
   * 自定义响应
   * @param code 状态码
   * @param message 响应消息
   * @param data 响应数据
   * @returns Response 实例
   */
  static custom<T>(code: number, message: string, data?: T): Response<T> {
    return new Response(code, message, data);
  }

  /**
   * 转换为普通对象
   * @returns 响应对象
   */
  toJSON(): IResponse<T> {
    return {
      code: this.code,
      message: this.message,
      data: this.data,
    };
  }
}
